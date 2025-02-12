def main():
  print("Hello learners!")


def trivia_fetch(num):
  num = input("Any number: ")

import json
import requests

number = requests.get("http://numbersapi.com/num?json")
triv = json.loads(number.content)



#`trivia_fetch(num)


if __name__=="__main__":
  main()
  trivia_fetch("42")