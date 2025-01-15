import streamlit as st
import random
import csv

#Initialize session state variables
if 'word' not in st.session_state:
    st.session_state.word=''
if 'guessed_letters' not in st.session_state:
    st.session_state.guessed_letters=[]
if 'attempts_left' not in st.session_state:
    st.session_state.attempts_left=6
if 'game_over' not in st.session_state:
    st.session_state.game_over=False
if 'game_started' not in st.session_state:
    st.session_state.game_started=False
if 'guess' not in st.session_state:
    st.session_state.guess=''
if 'difficulty' not in st.session_state:
    st.session_state.difficulty=''


#Function to reset the game
def reset_game():
    st.session_state.word=random.choice(word_list).upper()
    st.session_state.guessed_letters=[]
    st.session_state.attempts_left=7
    st.session_state.game_over=False
    st.session_state.game_started=True

#Function to select the difficulty of game
def select_difficulty():
    global word_list
    st.session_state.difficulty=st.selectbox('Select Difficulty:',['Easy','Medium','Hard'])
    with open(f'{st.session_state.difficulty}.txt','r') as f:
        word_list=f.read().split()

#Function to display the current state of the word
def display_word():
    if st.session_state.attempts_left==0:
        return st.session_state.word
    ans=[letter if letter in st.session_state.guessed_letters else '_' for letter in st.session_state.word]
    return ' '.join(ans)

#Function to draw the current state of the hangman
def draw_hangman():
    st.image(f'{st.session_state.attempts_left}.png')

#Function to guess an alphabet
def guess_letter(letter):
    if letter in st.session_state.guessed_letters:
        st.warning('You already guessed that letter')
    elif letter in st.session_state.word:
        st.session_state.guessed_letters.append(letter)
    else:
        st.session_state.guessed_letters.append(letter)
        st.session_state.attempts_left-=1

# Function to insert a score into the leaderboard
def insert_score(name,score):
    with open('leaderboard.csv','a') as f:
        writer=csv.writer(f)
        writer.writerow([name,st.session_state.difficulty,score])
    st.success('Record added to leaderboard')
    st.session_state.game_over=True

# Function to fetch leaderboard data
def fetch_leaderboard():
   with open('leaderboard.csv','r') as f:
       records=list(csv.DictReader(f))
       results=sorted(records,key=lambda x:int(x['Score']),reverse=True)
       return results

#Main Game
st.set_page_config(page_title='Hangman',page_icon='💀',layout='centered')
st.title('HANGMAN')
if not st.session_state.game_started:
    select_difficulty()

    #Button to start the game
    if st.button('Play'):
       reset_game()
       st.rerun()

    #Button to view leaderboard
    if st.button('View Leaderboard'):
        st.subheader("Leaderboard")
        leaderboard=fetch_leaderboard()
        if leaderboard:
            st.table(leaderboard)
        else:
            st.write("No scores yet!")

if st.session_state.game_started:
    st.markdown(f'# **Word: {display_word()}**')
    st.write(f"Guessed Letters: {', '.join(st.session_state.guessed_letters)}")
    st.write(f"Attempts left: {st.session_state.attempts_left}")
    draw_hangman()
    
    if not st.session_state.game_over:
        #Guessing an alphabet
        with st.form(key='Guess_form'):
            guess=st.text_input('Guess an alphabet:',max_chars=1).upper()
            submit_guess=st.form_submit_button(label='Submit Guess')
        if submit_guess and guess:
            st.session_state.guess=guess
            guess_letter(st.session_state.guess)
            st.rerun()

        #Check for win or loss
        if all(letter in st.session_state.guessed_letters for letter in st.session_state.word):
            st.success('🎉You win!!!')
            #Inputting username and inserting score to leaderboard
            with st.form(key='For_leaderboard'):
                name=st.text_input('Enter your name for the leaderboard:')
                submit_score=st.form_submit_button(label='Submit Score')
            if submit_score and name:
                insert_score(name,st.session_state.attempts_left)
        elif st.session_state.attempts_left<=0:
            st.error('Game over!')
            st.session_state.game_over=True

    #Restart game button
    if st.button('Restart Game'):
        st.session_state.game_started=False
        st.rerun()
