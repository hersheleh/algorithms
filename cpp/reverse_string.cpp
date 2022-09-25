#include <string>
#include <iostream>

using namespace std;

/*Takes a space serparated string as input and
  reverses each word
 */
string reverseWords(string s) {
  
  int word_start = 0;

  for (int i=0; i< s.length(); i++) {
    // calculate word length

    int word_end;

    if (s[i] == ' ' || i == s.length() - 1) {
      
      word_end = i-1;

      int word_length = word_end - word_start;
      while( word_start < word_end) {
        // swap indices
        char temp = s[word_end];
        s[word_end] = s[word_start];
        s[word_start] = temp;

        // move start index up and end index down
        word_start++;
        word_end--;
      }
      word_start = i + 1;
      cout << "string: " << s << endl;
    }

  }
  return "";
}

int main(int argc, char * argv[]) {
  reverseWords("what no back");

  return EXIT_SUCCESS;
}
