#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <iterator>
#include <stack>

using namespace std;
vector<int> Split(string str)
{
    vector<int> coins;
    int curr = 0;
    int prev = 0;
    curr = str.find(',');
    string substring;
    while (curr != string::npos) {
        substring = str.substr(prev,curr - prev);
        coins.push_back(atoi(substring.c_str()));
        prev = curr + 1;
        curr = str.find(',',prev);
    }
    substring = str.substr(prev,curr - prev);
    coins.push_back(atoi(substring.c_str()));
    return coins;
}

vector<int> EulerCycle(int start,map<int,vector<int>> graph)
{
    vector<int> answer;
    stack <int> vert_stack;
    vert_stack.push(start);
    while (!vert_stack.empty())
    {
        int v = vert_stack.top();
        if (graph[v].empty())
        {
            answer.push_back(v);
            vert_stack.pop();
        }
        else
        {
            vert_stack.push(graph[v][0]);
            graph[v].erase(graph[v].begin());
        }

    }
    return answer;
}

struct inOut
{
    int in;
    int out;
};

pair<int,int> inoutvert(map<int,vector<int>> graph)
{
    map <int,inOut> vertInOut; 
    for (auto it = graph.begin(); it != graph.end(); ++it)
    {
        int key = it->first;
        if (vertInOut.find(key) != vertInOut.end())
            vertInOut[key].out = it->second.size();
        else 
        {
            inOut st = { 0,it->second.size()};
            vertInOut[key] = st;
        }
        for (auto jt = it->second.begin(); jt != it->second.end(); ++jt) 
        {
            if (vertInOut.find(*jt) != vertInOut.end())
                vertInOut[*jt].in += 1;
            else 
            {
                inOut st = { 1,0 };
                vertInOut[*jt] = st;
            }
        }        
    }
    int from,to;
    for (auto it = vertInOut.begin(); it != vertInOut.end(); ++it) 
    {
        if (it->second.in > it->second.out)
            from = it->first;
        if (it->second.in < it->second.out)
            to = it->first;
    }
    return {from,to};
}

int main()
{
    map<int, vector<int>> graph;
    int vertex;
    string neighbours;
    while (cin >> vertex)
    {
        cin >> neighbours;
        cin >> neighbours;
        graph[vertex] = Split(neighbours);
    }
    pair<int, int> fromto = inoutvert(graph);
    graph[fromto.first].push_back(fromto.second);
    vector<int> answer = EulerCycle(vertex, graph);
    reverse(answer.begin(), answer.end());
    if (answer[0] == answer[answer.size() - 1])
        answer.pop_back();
    while (!(*answer.begin() == fromto.second && *(answer.end() - 1) == fromto.first))
    {
        std::vector<int>::iterator it = find(answer.begin() + 1, answer.end(), fromto.second);
        rotate(answer.begin(), it, answer.end());
    }  
    for (auto jt = answer.begin(); jt!=answer.end(); jt++)
    {
        if (jt!= answer.end()-1)
            cout << *jt << "->";
        else
            cout << *jt;
    }
}
