g++ -std=c++11 init.cpp -o init.so -fPIC -shared -pthread -O3 -march=native
g++ -std=c++11 test.cpp -o test.so -fPIC -shared -pthread -O3 -march=native
