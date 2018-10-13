# -AES-key-encoded-in-the-machine-readable-zone-of-a-European-ePassport
question：https://www.mysterytwisterc3.org/en/challenges/level-ii/aes-key--encoded-in-the-machine-readable-zone-of-a-european-epassport?showAll=1
1、	AES加密模式为CBC，初始化矢量即IV为零，填充为01-00）。此外，相应的密钥在身份证件上的机器可读区域（MRZ）等表格中，它与欧洲的电子护照一起使用时并不十分完整。
2、	目标是找到以下base64编码消息的明文：
9MgYwmuPrjiecPMx61O6zIuy3MtIXQQ0E59T3xB6u0Gyf1gYs2i3K9Jxaa0zj4gTMazJuApwd6+jdyeI5iGHvhQyDHGVlAuYTgJrbFDrfB22Fpil2NfNnWFBTXyf7SDI
3、	对于加密，已生成并应用基于基本访问控制（BAC）协议的密钥KENC。对于解密，已经发送了以下字符，从中可以导出KENC（这些字符的编码类型在[1]中描述）：
12345678 <8 <<< 1110182 <111116？<<<<<<<<<<<<<<< 4
4、	在传输过程中丢失了并且突出显示了一个''？''。可以在[2]的帮助下恢复它。
为了能够在之后计算密钥KENC，可以找到应用编码的概述
[3]，[4]中的协议和[5]中的一个例子。
5、	在解密之前解码base64代码。
6、	相关文献：
[1] ICAO MRTD DOC 9303 Part 1 Vol 1, p. IV-16 (Data structure of the lower machine readable line) and p. IV-42 
[2] ICAO MRTD DOC 9303 Part 1 Vol 1, p. IV-24 to IV-26 (Check digits in the machine readable zone) 
[3] ICAO MRTD DOC 9303 Part 1 Vol 2, p. IV-13 (MRTD Basic Access Control) [4] ICAO MRTD DOC 9303 Part 1 Vol 2, p. IV-32 
[5] ICAO MRTD DOC 9303 Part 1 Vol 2, p. IV-40 - IV-41


process：
A.	将已得密文base64解码得到新密文ciphertext
 
B.	还原mrz_information
根据下机读行数据结构,12345678 <8 <<< 1110182 <111116？<<<<<<<<<<<<<<< 4中的’?’代表到期日111116的校验位。
根据校验位计算法，在111116上重复731731加权后模10，所得即为校验位。
校验位计算代码如下：
 
得到结果 
即下机读行为 
C.	得到mrz_information
mrz_information= 护照号码 + 校验位 + 出生日期 + 校验位 + 到日期 + 校验位 
 
D.	得出密钥种子Kseed
对mrz_information做SHA1散列，取最高有效16位做密钥种子
 
E.	连接Kseed 和c得到D，并计算D的SHA1散列
 
F.	取h_D的最高有效16位为Ka，而后16位为Kb
 
G.	对Ka和Kb分别进行奇偶校验，得到新的k1和k2，真正密钥kenc=k1+k2
 
由于Ka和Kb为十六进制字符串，因此先将其转换为十进制再转换为2进制，8位一组分块，对每前7位做‘1’的计数，若为偶数，将最后一位赋值为‘1’，若为奇数，赋值为‘0’，再将左右块连接转换为16进制传回。
奇偶校检函数如下：
 
调用函数，得到真正的key
 
H.	利用AES.new(key，AES.MODE_CBC,IV).decrypt(ciphertext)函数解密新密文
由于题目中提到初始化矢量即IV为零，因此将IV设置为'0'*32
 
得到明文：Herzlichen Glueckwunsch. Sie haben die Nuss geknackt. Das Codewort lautet: Kryptographie!
