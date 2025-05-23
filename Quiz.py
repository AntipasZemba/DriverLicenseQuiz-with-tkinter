import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import time
import random

# --- User & Question Classes ---
class User:
    def __init__(self, first_name, last_name, id_number, age):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number
        self.age = age

