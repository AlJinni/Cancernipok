x=`ps -ef | grep python | wc -l`
let  x+=-1
echo $x
