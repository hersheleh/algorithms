#include <cstdlib>
#include <cstring>
#include <sstream>
#include <string>
#include <iostream>
#include <cstring>

using namespace std;


string reverseWords_getline(string s) {
  string token;
  istringstream iss(s);
  string output;

  while (getline(iss, token, ' ')) {

    int word_start = 0;
    int word_end = token.length() - 1;

    while(word_start < word_end) {

      char temp = token[word_start];
      token[word_start] = token[word_end];
      token[word_end] = temp;
      word_start++;
      word_end--;
    }
    output += token + " ";
  }
  return output.substr(0, s.length());
}

/* Reverses each word in a space serparated string */
string reverseWords(string s) {

  char i_string[s.length()+1];
  strcpy(i_string, s.c_str());
  cout << i_string << endl;

  // for (int i = 0; i < s.length(); i++) {
  //   i_string[i] = s[i];
  // }

  int word_start = 0;
  int word_end;
  int end_of_string = s.length() - 1; // the last character
  char current_char;
  char next_char;

  for (int i=0; i< s.length(); i++) {
    /* when we reach a space or end of string
     begin swapping letters*/

    current_char = i_string[i];        // the current char
    next_char = i_string[i+1];         // The char after this one
    cout << "something random" << endl;
    cout << next_char << endl;

    if (next_char == ' ' || i == end_of_string) {

      word_end = i;

      while( word_start < word_end) {
        // swap indicese
        char temp = i_string[word_end];
        i_string[word_end] = i_string[word_start];
        i_string[word_start] = temp;

        cout << i_string << endl;

        // move start index up and end index down
        word_start++;
        word_end--;
      }
      word_start = i + 2;
    }


  }
  return s;
}

int main(int argc, char * argv[]) {
  // string out = reverseWords_getline("Let's take LeetCode contest");
  // cout << out << endl;

  string result = reverseWords("Let's take LeetCode contest");
  cout << result << endl;

  return EXIT_SUCCESS;
}
