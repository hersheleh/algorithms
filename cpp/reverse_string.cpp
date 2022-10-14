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

/*Takes a space serparated string as input and
  reverses each word */
string reverseWords(string s) {
  // char i_string[s.length()+1];
  char *i_string = &s[0];
  int word_start = 0;
  int word_end;

  for (int i=0; i< s.length(); i++) {

    /* when we reach a space or end of string
     begin swapping letters*/
    if (s[i+1] == ' ' || i == s.length() - 1) {

      word_end = i;

      int word_length = word_end - word_start;

      while( word_start < word_end) {
        // swap indices
        char temp = s[word_end];
        s[word_end] = s[word_start];
        s[word_start] = temp;
        i_string = &s[0];
        // strcpy(i_string, s.c_str());
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
