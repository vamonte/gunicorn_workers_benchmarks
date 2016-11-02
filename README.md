# Benchmark

To run the environment (4 workers):

```sh
  # sync worker
  git checkout master
  docker-compose build && docker-compose up
  # gevent worker
  git checkout gevent
  docker-compose build && docker-compose up
```


## I - Simple json response:

Benchmark on a view that build and return a very simple json.

Used command:
```sh
  ab -c {concurrency number} -n 1000 http://localhost:800[0|1]/simple_json
```

### A - Sync worker
| concurrency number   | Tot  time (sc) | rq/sc       |
| :---:                | :---:          | :---:       |
|         **4**        |    0.871       |  1147.95    |
|         **4**        |    0.847       |  1180.07    |
|         **4**        |    0.937       |  1067.35    |
|         **4**        |    0.871       |  1148.30    |
|         **4**        |    0.891       |  1121.90    |

|         Average      |    0.883       |  1133,114   |
| :---:                | :---:          | :---:       |


| concurrency number   | Tot  time (sc) | rq/sc       |
| :---:                | :---:          | :---:       |
|         **8**        |    0.699       |  1429.80    |
|         **8**        |    0.737       |  1355.96    |
|         **8**        |    0.665       |  1504.59    |
|         **8**        |    0.728       |  1374.34    |
|         **8**        |    0.771       |  1297.38    |

|         Average      |    0.720       |  1392,414   |
| :---:                | :---:          | :---:       |

| concurrency number   | Tot  time (sc) | rq/sc       |
| :---:                | :---:          | :---:       |
|         **16**       |    0.665       |  1503.45    |
|         **16**       |    0.629       |  1588.56    |
|         **16**       |    0.631       |  1584.41    |
|         **16**       |    0.669       |  1495.52    |
|         **16**       |    0.644       |  1553.03    |

|         Average      |    0.648       |  1544,994   |
| :---:                | :---:          | :---:       |

### B - Gevent worker

| concurrency number   | Tot  time (sc) | rq/sc       |
| :---:                | :---:          | :---:       |
|         **4**        |    1.102       |  907.31     |
|         **4**        |    1.139       |  877.88     |
|         **4**        |    1.216       |  822.42     |
|         **4**        |    1.141       |  876.51     |
|         **4**        |    1.199       |  833.75     |

|         Average      |    1.159       |  863,574    |
| :---:                | :---:          | :---:       |


| concurrency number   | Tot  time (sc) | rq/sc       |
| :---:                | :---:          | :---:       |
|         **8**        |    1.037       |  964.56     |
|         **8**        |    1.125       |  889.07     |
|         **8**        |    1.141       |  876.81     |
|         **8**        |    1.017       |  983.36     |
|         **8**        |    1.030       |  971.28     |

|         Average      |    1.070       |  937,016    |
| :---:                | :---:          | :---:       |

| concurrency number   | Tot  time (sc) | rq/sc       |
| :---:                | :---:          | :---:       |
|         **16**       |    1.018       |  982.41     |
|         **16**       |    0.956       |  1045.79    |
|         **16**       |    1.095       |  913.20     |
|         **16**       |    1.053       |  949.93     |
|         **16**       |    1.069       |  935.22     |

|         Average      |    1,038       |  965,31     |
| :---:                | :---:          | :---:       |


### __Conclusion :__

Gevents seems to be slower.
 
Why? **_In progress..._**


## II - External request before response:

Benchmark on a view that make an external request before to build and to return an HTTP response.

Used command:
```sh
  ab -c {concurrency number} -n 1000 http://localhost:800[0|1]/simple_request/0
```

### A - Sync worker
| concurrency number   | Tot  time (sc) | rq/sc       |
| :---:                | :---:          | :---:       |
|         **4**        |    30.373      |  32.92      |
|         **4**        |    30.885      |  32.38      |
|         **4**        |    30.741      |  32.53      |
|         **4**        |    29.430      |  33.98      |
|         **4**        |    30.797      |  32.47      |

|         Average      |    30.439      |  32,856     |
| :---:                | :---:          | :---:       |


| concurrency number   | Tot  time (sc) | rq/sc       |
| :---:                | :---:          | :---:       |
|         **8**        |    29.976      |  33.36      |
|         **8**        |    29.621      |  33.76      |
|         **8**        |    30.777      |  32.49      |
|         **8**        |    29.645      |  33.73      |
|         **8**        |    29.602      |  33.78      |

|         Average      |    29,924      |  33,424     |
| :---:                | :---:          | :---:       |

| concurrency number   | Tot  time (sc) | rq/sc       |
| :---:                | :---:          | :---:       |
|         **16**       |    29.449      |  33.96      |
|         **16**       |    29.121      |  34.34      |
|         **16**       |    30.118      |  33.20      |
|         **16**       |    29.204      |  34.24      |
|         **16**       |    29.030      |  34.45      |

|         Average      |    29.384      |  34,038     |
| :---:                | :---:          | :---:       |


### B - Gevent worker

| concurrency number   | Tot  time (sc) | rq/sc       |
| :---:                | :---:          | :---:       |
|         **4**        |    30.487      |  32.80      |
|         **4**        |    30.757      |  32.51      |
|         **4**        |    30.843      |  32.42      |
|         **4**        |    29.095      |  34.37      |
|         **4**        |    29.689      |  33.68      |

|         Average      |    30.174      |  33,156     |
| :---:                | :---:          | :---:       |


| concurrency number   | Tot  time (sc) | rq/sc       |
| :---:                | :---:          | :---:       |
|         **8**        |    15.452      |  64.72      |
|         **8**        |    15.002      |  66.66      |
|         **8**        |    15.141      |  66.05      |
|         **8**        |    15.124      |  66.12      |
|         **8**        |    15.290      |  65.40      |

|         Average      |    15,202      |  65,790     |
| :---:                | :---:          | :---:       |

| concurrency number   | Tot  time (sc) | rq/sc       |
| :---:                | :---:          | :---:       |
|         **16**       |    7.967       |  125.51     |
|         **16**       |    7.385       |  135.42     |
|         **16**       |    7.479       |  133.71     |
|         **16**       |    7.704       |  129.81     |
|         **16**       |    7.772       |  128.67     |

|         Average      |    7,661       |  130,624    |
| :---:                | :---:          | :---:       |


### __Conclusion :__

_Not yet..._
 

## II - Save data in postgres data before response:

Benchmark on a view that save some data in postgres before to build and to return an HTTP response.

Used command:
```sh
  ab -c {concurrency number} -n 1000 http://localhost:800[0|1]/create_data/1
```

### A - Sync worker
| concurrency number   | Tot  time (sc) | rq/sc       |
| :---:                | :---:          | :---:       |
|         **4**        |    6.475       |  154.43     |
|         **4**        |    6.384       |  156.63     |
|         **4**        |    6.385       |  156.61     |
|         **4**        |    6.453       |  154.97     |
|         **4**        |    6.565       |  152.33     |

|         Average      |    6.452       |  154.994    |
| :---:                | :---:          | :---:       |


| concurrency number   | Tot  time (sc) | rq/sc       |
| :---:                | :---:          | :---:       |
|         **8**        |    7.288       |  137.21     |
|         **8**        |    6.695       |  149.38     |
|         **8**        |    6.563       |  152.38     |
|         **8**        |    6.379       |  156.75     |
|         **8**        |    6.482       |  154.27     |

|         Average      |    6.681       |  149.998     |
| :---:                | :---:          | :---:       |

| concurrency number   | Tot  time (sc) | rq/sc       |
| :---:                | :---:          | :---:       |
|         **16**       |    6.484       |  154.23     |
|         **16**       |    7.468       |  133.90     |
|         **16**       |    6.446       |  155.14     |
|         **16**       |    6.404       |  156.16     |
|         **16**       |    6.718       |  148.85     |

|         Average      |    6,704       |  149.656    |
| :---:                | :---:          | :---:       |


### A - Gevent worker (MAC_CONNS=10)
| concurrency number   | Tot  time (sc) | rq/sc       |
| :---:                | :---:          | :---:       |
|         **4**        |    7.089       |  141.06     |
|         **4**        |    6.938       |  144.13     |
|         **4**        |    6.892       |  145.10     |
|         **4**        |    6.795       |  147.17     |
|         **4**        |    6.995       |  142.96     |

|         Average      |    6.942       |  144,084    |
| :---:                | :---:          | :---:       |


| concurrency number   | Tot  time (sc) | rq/sc       |
| :---:                | :---:          | :---:       |
|         **8**        |    4.725       |  211.64     |
|         **8**        |    4.677       |  213.80     |
|         **8**        |    4.676       |  213.87     |
|         **8**        |    4.494       |  222.52     |
|         **8**        |    4.828       |  207.15     |

|         Average      |    4,680       |  213,796    |
| :---:                | :---:          | :---:       |

| concurrency number   | Tot  time (sc) | rq/sc       |
| :---:                | :---:          | :---:       |
|         **16**       |    3.217       |  310.89     |
|         **16**       |    3.275       |  305.34     |
|         **16**       |    3.090       |  323.59     |
|         **16**       |    3.341       |  299.31     |
|         **16**       |    3.302       |  302.89     |

|         Average      |    3.245       |  308.404    |
| :---:                | :---:          | :---:       |


### __Conclusion :__

_Not yet..._
