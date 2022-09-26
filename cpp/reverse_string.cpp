#include <cstring>
#include <string>
#include <iostream>
#include <cstring>

using namespace std;

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

  reverseWords("Let's take LeetCode contest");

  return EXIT_SUCCESS;
}
