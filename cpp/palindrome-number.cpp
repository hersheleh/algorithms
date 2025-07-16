#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
  static bool isEven(int x) {
    if (x % 2 == 0) {
      return true;
    }
    else {
      return false;
    }
  };
  bool isPalindromeStack(int x) {
    string xStr = to_string(x);
    int stackPtr = -1;
    char stack[100];
    int i=0;
    int strLen = xStr.length();
    while(i<strLen / 2) {
      stackPtr++;
      stack[stackPtr] = xStr[i];
      i++;
    }
    if (!isEven(strLen)) {
      i++;
    }
    while (i< strLen) {
      if (stack[stackPtr] == xStr[i]) {
        i++;
        stackPtr--;
        continue;
      } else {
        return false;
      }
    }
    return true;
  }

  bool isPalindromeComp(int x) {
    string xStr = to_string(x);
    int i=0;
    int j=xStr.length() -1;
    while (i < xStr.length() / 2) {
      if (xStr[i] == xStr[j]) {
        // cout << "comp " << xStr[i] << " & " << xStr[j] << endl;
        i++;
        j--;
        continue;
      } else {
        return false;
      }
    }
    return true;
  }
};

int main() {
  Solution * s = new Solution();
  int pLen = 5;
  int problems[] = {1, 11, 121, -121, 345};
  for (int i = 0; i< pLen; i++) {
    cout << "check: " << problems[i] << endl;
    cout << "comp: " << s->isPalindromeComp(problems[i]) << endl;
    cout<< "stack: " << s->isPalindromeStack(problems[i]) << endl;
    cout << "------------------------------------" << endl;
  }

  return 0;
}
