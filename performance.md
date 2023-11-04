# nginx


This is ApacheBench, Version 2.3 <$Revision: 1879490 $><br/>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/<br/>
Licensed to The Apache Software Foundation, http://www.apache.org/<br/>

Benchmarking 127.0.0.1 (be patient)<br/>
Completed 100 requests<br/>
Completed 200 requests<br/>
Completed 300 requests<br/>
Completed 400 requests<br/>
Completed 500 requests<br/>
Completed 600 requests<br/>
Completed 700 requests<br/>
Completed 800 requests<br/>
Completed 900 requests<br/>
Completed 1000 requests<br/>
Finished 1000 requests<br/>


Server Software:        nginx/1.18.0<br/>
Server Hostname:        127.0.0.1<br/>
Server Port:            8001<br/>

Document Path:          /<br/>
Document Length:        42 bytes<br/>

Concurrency Level:      100
Time taken for tests:   0.061 seconds<br/>
Complete requests:      1000<br/>
Failed requests:        70<br/>
   (Connect: 0, Receive: 0, Length: 35, Exceptions: 35)<br/>
Total transferred:      272130 bytes<br/>
HTML transferred:       40530 bytes<br/>
Requests per second:    16496.21 [#/sec] (mean)<br/>
Time per request:       6.062 [ms] (mean)<br/>
Time per request:       0.061 [ms] (mean, across all concurrent requests)<br/>
Transfer rate:          4383.90 [Kbytes/sec] received<br/>

Connection Times (ms)

 label     |  min | mean[+/-sd]| median  | max|
-----------|------|------------|---------|----|            
Connect    |    0 |   2   1.3  |    2    |   6|
Processing |    1 |   3   1.8  |    3    |   8|
Waiting    |    0 |   3   1.5  |    2    |   7|
Total      |    2 |   6   2.8  |    4    |  11|

Percentage of the requests served within a certain time (ms)

  50%      4 <br/>
  66%      7 <br/>
  75%      9 <br/>
  80%      9 <br/>
  90%     10 <br/>
  95%     10 <br/>
  98%     11 <br/> 
  99%     11 <br/>
 100%     11 (longest request) <br/>



# gunicorn 

 This is ApacheBench, Version 2.3 <$Revision: 1879490 $><br/>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/<br/>
Licensed to The Apache Software Foundation, http://www.apache.org/<br/>

Benchmarking 127.0.0.1 (be patient)<br/>
Completed 100 requests<br/>
Completed 200 requests<br/>
Completed 300 requests<br/>
Completed 400 requests<br/>
Completed 500 requests<br/>
Completed 600 requests<br/>
Completed 700 requests<br/>
Completed 800 requests<br/>
Completed 900 requests<br/>
Completed 1000 requests<br/>
Finished 1000 requests<br/>


Server Software:        gunicorn<br/>
Server Hostname:        127.0.0.1<br/>
Server Port:            8002<br/>

Document Path:          /<br/>
Document Length:        11 bytes<br/>

Concurrency Level:      100<br/>
Time taken for tests:   0.152 seconds<br/>
Complete requests:      1000<br/>
Failed requests:        0<br/>
Total transferred:      150000 bytes<br/>
HTML transferred:       11000 bytes<br/>
Requests per second:    6597.96 [#/sec] (mean)<br/>
Time per request:       15.156 [ms] (mean)<br/>
Time per request:       0.152 [ms] (mean, across all concurrent requests)<br/>
Transfer rate:          966.50 [Kbytes/sec] received<br/>

Connection Times (ms)<br/>
label       |    min | mean[+/-sd]| median |  max<br/>|
------------|--------|------------|--------|----------|
Connect:    |    0   | 0   0.9    |  0     |  4<br/>  |
Processing: |    2   |14   3.2    | 14     | 20<br/>  |
Waiting:    |    1   |14   3.2    | 14     | 20<br/>  |
Total:      |    6   |14   2.9    | 14     | 21<br/>  |

Percentage of the requests served within a certain time (ms)<br/>
  50%     14<br/>
  66%     15<br/>
  75%     16<br/>
  80%     17<br/>
  90%     19<br/>
  95%     19<br/>
  98%     20<br/>
  99%     20<br/>
 100%     21 (longest request)<br/>