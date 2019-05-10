# the challenge of MT3-mysterytwisterc3
question1-AES-key-encoded-in-the-machine-readable-zone-of-a-European-ePassport——huzhao.py <br>
https://www.mysterytwisterc3.org/en/challenges/level-ii/aes-key--encoded-in-the-machine-readable-zone-of-a-european-epassport?showAll=1 <br>
1、	AES加密模式为CBC，初始化矢量即IV为零，填充为01-00）。此外，相应的密钥在身份证件上的机器可读区域（MRZ）等表格中，它与欧洲的电子护照一起使用时并不十分完整。<br>
2、	目标是找到以下base64编码消息的明文：<br>
9MgYwmuPrjiecPMx61O6zIuy3MtIXQQ0E59T3xB6u0Gyf1gYs2i3K9Jxaa0zj4gTMazJuApwd6+jdyeI5iGHvhQyDHGVlAuYTgJrbFDrfB22Fpil2NfNnWFBTXyf7SDI<br>
3、	对于加密，已生成并应用基于基本访问控制（BAC）协议的密钥KENC。对于解密，已经发送了以下字符，从中可以导出KENC（这些字符的编码类型在[1]中描述）：
12345678 <8 <<< 1110182 <111116？<<<<<<<<<<<<<<< 4<br>
4、	在传输过程中丢失了并且突出显示了一个''？''。可以在[2]的帮助下恢复它。<br>
为了能够在之后计算密钥KENC，可以找到应用编码的概述<br>
[3]，[4]中的协议和[5]中的一个例子。<br>
5、	在解密之前解码base64代码。<br>

A.	将已得密文base64解码得到新密文ciphertext<br>
B.	还原mrz_information<br>
根据下机读行数据结构,12345678 <8 <<< 1110182 <111116？<<<<<<<<<<<<<<< 4中的’?’代表到期日111116的校验位。<br>
根据校验位计算法，在111116上重复731731加权后模10，所得即为校验位。<br>
校验位计算代码如下：<br>
C.	得到mrz_information<br>
mrz_information= 护照号码 + 校验位 + 出生日期 + 校验位 + 到日期 + 校验位 <br>
D.	得出密钥种子Kseed<br>
对mrz_information做SHA1散列，取最高有效16位做密钥种子<br>
E.	连接Kseed 和c得到D，并计算D的SHA1散列<br>
F.	取h_D的最高有效16位为Ka，而后16位为Kb<br>
G.	对Ka和Kb分别进行奇偶校验，得到新的k1和k2，真正密钥kenc=k1+k2<br>
 
由于Ka和Kb为十六进制字符串，因此先将其转换为十进制再转换为2进制，8位一组分块，对每前7位做‘1’的计数，若为偶数，将最后一位赋值为‘1’，若为奇数，赋值为‘0’，再将左右块连接转换为16进制传回。<br>
奇偶校检函数如下：<br>
调用函数，得到真正的key<br>
H.	利用AES.new(key，AES.MODE_CBC,IV).decrypt(ciphertext)函数解密新密文<br>
由于题目中提到初始化矢量即IV为零，因此将IV设置为'0'*32<br>
 
得到明文：Herzlichen Glueckwunsch. Sie haben die Nuss geknackt. Das Codewort lautet: Kryptographie<br>

question2：Cracking SHA1-Hashed Passwords——crack_sha1.py<br>
https://www.mysterytwisterc3.org/en/challenges/level-ii/cracking-sha1-hashed-passwords<br>
很简单<br>
优化后代码：<br>
bettersha1.py<br>
### 如果对你有帮助的话，请点赞哦<br>
