def main():
  print("Hello learners!")


def trivia_fetch(num):
  num = input("Any number: ")

import json
import requests
import random

number = requests.get("http://numbersapi.com/random?json")
triv = json.loads(number.content)



#`trivia_fetch(num)


if __name__=="__main__":
  main()
  trivia_fetch("42")