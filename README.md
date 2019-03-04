# txporn
txporn converts text to png image whose background is transparent.

# Requirement
- Python 3
- Pillow 5.0.0

# Install

```
$ git clone https://github.com/opqrstuvcut/txporn.git
$ pip install Pillow
```

# Example
```$ ./txporn.py -t かつお -c red -o ./output/ -s 50``` 

output:

![かつお](./output/かつお.png)

You can specify font name or font file path as below.

```$ ./txporn.py -t IKURA -c orange -o ./output/ -s 50 -f Times``` 

output:

![IKURA](./output/IKURA.png)

You can also specify transparency of text.

```$ ./txporn.py -t さざえ -c green -o ./output/ -s 50 -a 0.5``` 

output:

![さざえ](./output/さざえ.png)
