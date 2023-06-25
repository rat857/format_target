# format_target
格式化未带请求头的url

### 背景：

由于空间搜索引擎搜索出来的目标有些混乱，有的带http://和https://而有的却没有，这就对于像我这种nuclei重度依赖症患者很难受

因为nuclei扫时，只识别带了协议头的，而像114.114.114.114这种直接不管不顾、



BUT有了这个工具他会自动格式化114.114.114.114成http://144.144.144.144



### 食用方法：

```shell
git clone https://github.com/rat857/format_target.git
cd format_target
python3 format.py -h

python3 format.py -i your.txt -o end.txt	#your.txt是你的混合文件，end.txt是格式化后的文件名
```

然后直接：

```shell
nuclei -l end.txt
```

### shodan_API的配合方法

```shell
shodan download --limit -1 fav http.favicon.hash:-911494769 #fav为保存的文件名，最终会保存为fav.json.gz,这一行是从shodan官网下载下来目标数据
shodan parse --fields ip_str,port fav.json.gz > 1.txt #解析下载下来的数据
cat 1.txt | sed s/[[:space:]]/:/g > target.txt
python3 format.py -i target.txt -o end.txt
```
