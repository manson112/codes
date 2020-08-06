#include<memory.h>
#include<cstdio>
#include<queue>
#include<utility>
#define ABS(x) ( x > 0 ? x : -(x))

using namespace std;
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};
int N, L, R;
int A[2501] = {0};
bool visited[2501];
int sum, ans, cnt;
queue<int> que;

void dfs(int index) {
    for(int i=0; i<4; ++i) {
        int nx = index/N + dx[i];
        int ny = index%N + dy[i];
        int newIndex = N*nx + ny;
        if (visited[newIndex] || nx < 0 || ny < 0 || nx >= N || ny >= N ) continue;
        int diff = ABS(A[index] - A[newIndex]);
        if (diff >= L && diff <= R) {
            visited[newIndex] = true;
            sum += A[newIndex];
            que.push(newIndex);
            cnt++;
            dfs(newIndex);
        }
    }
}

int main() {
    scanf("%d %d %d", &N, &L, &R);

    for(int i=0; i<N*N; ++i) {
        int tmp;
        scanf("%d", &tmp);
        A[i] = tmp;
    }

    while (true) {
        bool flag = false;
        memset(visited, false, sizeof(visited));
        for (int i=0; i<N*N; ++i) {
            if(visited[i]) continue;
            visited[i] = true;
            sum = A[i];
            cnt = 1;
            while(!que.empty()) que.pop();
            que.push(i);
            dfs(i);
            if (cnt > 1) {
                flag = true;
                int sizeOfQ = que.size();
                for(int j=0; j<sizeOfQ; ++j){
                    int cp = que.front();
                    que.pop();
                    A[cp] = sum / sizeOfQ;
                }
            }
        }
        if (!flag) break;
        ans++;
    }

    printf("%d", ans);



    return 0;
}