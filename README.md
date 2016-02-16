Simple wrapper using ctypes in Python for the [Haraka](https://github.com/kste/haraka) hash function.

Testing is as simple as:

```text
make
python3.5 ./test.py
```

> Note: You _need_ a processor with the appropriate SSE and AES instructions.
> For example my 2nd gen i3 can't run it but my 3rd gen i5 can.
