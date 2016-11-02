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


## 1) Simple json response:

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

