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
| concurrency number   | resp time (sc) | rq/sc       |
| :---:                | :---:          | :---:       |
|         **4**        |    0.871       |  1147.95    |
|         **4**        |    0.847       |  1180.07    |
|         **4**        |    0.937       |  1067.35    |
|         **4**        |    0.871       |  1148.30    |
|         **4**        |    0.891       |  1121.90    |

|         Average      |    0.883       |  1133,114   |
| :---:                | :---:          | :---:       |


| concurrency number   | resp time (sc) | rq/sc       |
| :---:                | :---:          | :---:       |
|         **8**        |    0.699       |  1429.80    |
|         **8**        |    0.737       |  1355.96    |
|         **8**        |    0.665       |  1504.59    |
|         **8**        |    0.728       |  1374.34    |
|         **8**        |    0.771       |  1297.38    |

|         Average      |    0.720       |  1392,414   |
| :---:                | :---:          | :---:       |

| concurrency number   | resp time (sc) | rq/sc       |
| :---:                | :---:          | :---:       |
|         **16**       |    0.665       |  1503.45    |
|         **16**       |    0.629       |  1588.56    |
|         **16**       |    0.631       |  1584.41    |
|         **16**       |    0.669       |  1495.52    |
|         **16**       |    0.644       |  1553.03    |

|         Average      |    0.648       |  1544,994   |
| :---:                | :---:          | :---:       |

### B - Gevent worker

| concurrency number   | resp time (sc) | rq/sc       |
| :---:                | :---:          | :---:       |
|         **4**        |    1.102       |  907.31     |
|         **4**        |    1.139       |  877.88     |
|         **4**        |    1.216       |  822.42     |
|         **4**        |    1.141       |  876.51     |
|         **4**        |    1.199       |  833.75     |

|         Average      |    1.159       |  863,574    |
| :---:                | :---:          | :---:       |


| concurrency number   | resp time (sc) | rq/sc       |
| :---:                | :---:          | :---:       |
|         **8**        |    1.037       |  964.56     |
|         **8**        |    1.125       |  889.07     |
|         **8**        |    1.141       |  876.81     |
|         **8**        |    1.017       |  983.36     |
|         **8**        |    1.030       |  971.28     |

|         Average      |    1.070       |  937,016    |
| :---:                | :---:          | :---:       |

| concurrency number   | resp time (sc) | rq/sc       |
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
| concurrency number   | resp time (sc) | rq/sc       |
| :---:                | :---:          | :---:       |
|         **4**        |    30.373      |  32.92      |
|         **4**        |    30.885      |  32.38      |
|         **4**        |    30.741      |  32.53      |
|         **4**        |    29.430      |  33.98      |
|         **4**        |    30.797      |  32.47      |

|         Average      |    30.439      |  32,856     |
| :---:                | :---:          | :---:       |


| concurrency number   | resp time (sc) | rq/sc       |
| :---:                | :---:          | :---:       |
|         **8**        |    29.976      |  33.36      |
|         **8**        |    29.621      |  33.76      |
|         **8**        |    30.777      |  32.49      |
|         **8**        |    29.645      |  33.73      |
|         **8**        |    29.602      |  33.78      |

|         Average      |    29,924      |  33,424     |
| :---:                | :---:          | :---:       |

| concurrency number   | resp time (sc) | rq/sc       |
| :---:                | :---:          | :---:       |
|         **16**       |    29.449      |  33.96      |
|         **16**       |    29.121      |  34.34      |
|         **16**       |    30.118      |  33.20      |
|         **16**       |    29.204      |  34.24      |
|         **16**       |    29.030      |  34.45      |

|         Average      |    29.384      |  34,038     |
| :---:                | :---:          | :---:       |


### B - Gevent worker

| concurrency number   | resp time (sc) | rq/sc       |
| :---:                | :---:          | :---:       |
|         **4**        |    30.487      |  32.80      |
|         **4**        |    30.757      |  32.51      |
|         **4**        |    30.843      |  32.42      |
|         **4**        |    29.095      |  34.37      |
|         **4**        |    29.689      |  33.68      |

|         Average      |    30.174      |  33,156     |
| :---:                | :---:          | :---:       |


| concurrency number   | resp time (sc) | rq/sc       |
| :---:                | :---:          | :---:       |
|         **8**        |    15.452      |  64.72      |
|         **8**        |    15.002      |  66.66      |
|         **8**        |    15.141      |  66.05      |
|         **8**        |    15.124      |  66.12      |
|         **8**        |    15.290      |  65.40      |

|         Average      |    15,202      |  65,790     |
| :---:                | :---:          | :---:       |

| concurrency number   | resp time (sc) | rq/sc       |
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
 
