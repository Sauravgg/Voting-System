import tkinter as tk
from tkinter import messagebox

class VotingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title('Voting Management System')

        # Dummy data for authentication and candidates
        self.users = {'Amit': 'pps', 'Saurav': 'oops'}
        self.candidates = {'1': 'Rsp', '2': 'Bjp'}

        # Start the voting process
        self.start()

    def start(self):
        # Display welcome message and instructions
        messagebox.showinfo('Welcome', 'Welcome to the Python Voting Management System. Please enter your username and password to vote.')

        # Create and pack widgets for username and password input
        self.username_label = tk.Label(self.root, text='Votername:')
        self.username_entry = tk.Entry(self.root)
        self.password_label = tk.Label(self.root, text='Password:')
        self.password_entry = tk.Entry(self.root, show='@')
        self.login_button = tk.Button(self.root, text='Login', command=self.authenticate_user)

        self.username_label.pack()
        self.username_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.login_button.pack()

    def authenticate_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in self.users and self.users[username] == password:
            # If the username and password are valid
            self.display_candidates()
        else:
            # If the Votername and password are invalid
            messagebox.showerror('Error', 'Invalid Votername or password. Please try again.')

    def display_candidates(self):
        # Fetch the list of candidates from the database and display them to the user
        self.candidate_label = tk.Label(self.root, text='Candidates:')
        self.candidate_label.pack()

        for id, name in self.candidates.items():
            button = tk.Button(self.root, text=name, command=lambda id=id: self.vote(id))
            button.pack()

    def vote(self, candidate_id):
        # Validate the selected candidate and submit the vote to the database
        if candidate_id in self.candidates:
            # If the candidate ID is valid
            confirm = messagebox.askyesno('Confirm', f'You have selected {self.candidates[candidate_id]}. Do you want to confirm your vote?')

            if confirm:
                # If the vote submission is successful
                messagebox.showinfo('Success', 'Your vote has been successfully submitted. Thank you for voting.')
                self.root.quit()
            else:
                # If the vote submission is unsuccessful
                messagebox.showerror('Error', 'There was an error submitting your vote. Please try again.')
        else:
            # If the candidate ID is invalid
            messagebox.showerror('Error', 'Invalid candidate ID. Please select a valid candidate.')

root = tk.Tk()
app = VotingSystem(root)
root.mainloop()
