import json
import requests

def trivia_fetch(number):
  response = requests.get(f"http://numbersapi.com/{number}/trivia?json")
  return response.json()

def main():
  print("Hello learners!")
  print("Welcome to the Number Trivia Quiz!")
  num = int(input("Enter any number to get a trivia: "))
  trivia = trivia_fetch(num)
  print(trivia)


if __name__=="__main__":
  main()