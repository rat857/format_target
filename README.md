# format_target

### 背景：

由于fofa搜索出来的目标有些混乱，有的带http://和https://而有的却没有，这就对于像我这种nuclei重度依赖症患者很难受

因为nuclei扫时，只识别带了协议头的，而像114.114.114.114这种直接不管不顾、



BUT有了这个工具他会自动格式化114.114.114.114成http://144.144.144.144



### 食用方法：

```shell
python3 format.py -h

python3 format.py -i your.txt -o end.txt	#your.txt是你的混合文件，end.txt是格式化后的文件名
```

然后直接：

```shell
nuclei -l end.txt
```

