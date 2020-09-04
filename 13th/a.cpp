#include <iostream>
#include <vector>
#include <cstring>

#include <fstream>

using namespace std;



int N, C, M;

int post[2001] = { 0 };
int receive[2001] = { 0 };

int box_sum = 0;
int res = 0;
int main(void)
{
   ifstream in("input.txt");
   in >> N >> C >> M;
   
   for (int i = 0; i < M; ++i)
   {
      int s, d, box;
      in >> s >> d >> box;
      post[s] += box;
      receive[d] += box;
   }

   for (int i = 1; i <= N; ++i)
   {
      if (box_sum - receive[i] < 0) {
         res += box_sum; // 다 줘버리고.
         box_sum = 0;
      }
      else {
         res += receive[i];
         box_sum -= receive[i];
      }

      if (box_sum + post[i] > C) box_sum = C;
      else box_sum += post[i];
   }
   cout << res << endl;

}