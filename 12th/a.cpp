#include <iostream>
#include <vector>

using namespace std;

int N,MAP[51][9], line[9], ans;
bool check[10], base[5];
vector<int> lineup;

void calc()
{
	for(int i=0;i<5;i++)
		base[i] = false;

	int batter = 0, score = 0;
	for(int inning=0;inning<N;inning++)
	{
		for(int out=0;out<3;)
		{
			batter = (batter) % 9;
			if(MAP[inning][line[batter]] == 0)
			{
				out++;
			}
			else
			{
				switch(MAP[inning][line[batter]]){
					case 1: //1루타
						if(base[3]) score++;
						base[3] = base[2];
						base[2] = base[1];
						base[1] = true;

					break;
					case 2: //2루타
						for(int i=2;i<=3;i++) //2, 3루 불러들이기
						{
							if(base[i]){
								base[i] = false;
								score++;
							}
						}
						if(base[1])
						{
							base[3] = true;
							base[1] = false;
						}
						base[2] = true; //타자주자 2주까지
					break;
					case 3: //3루타
						for(int i=1;i<=3;i++)
						{
							if(base[i])
							{
								base[i] = false;
								score++;
							}
						}
						base[3] = true;
					break;
					case 4: //홈런
					for(int i=1;i<=3;i++)
						if (base[i]){
							base[i] = false;
							score++;
						}
					score++;
					break;
				}
			}
			batter++;
		}
		for(int i=0;i<5;i++)
			base[i] = false; //이닝이 끝나면 베이스 초기화
	}

	if(score > ans) ans = score;
}

void solve()
{
	if(lineup.size() == 8)
	{
		for(int i=0;i<9;i++)
		{
			if(i<3) line[i] = lineup[i];
			else if(i == 3) line[i] = 0;
			else line[i] = lineup[i-1];
		}
		calc();
		return;
	}

	for(int i=1;i<9;i++)
	{
		if(!check[i])
		{
			check[i] = true;
			lineup.push_back(i);

			solve();

			check[i] = false;
			lineup.pop_back();

		}
	}

}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);cout.tie(0);

	cin>>N;
	for(int i=0;i<N;i++)
		for(int j=0;j<9;j++)
			cin>>MAP[i][j];
	
	check[0] = true;
	solve();
	cout<<ans;
    return 0;
}