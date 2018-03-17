# a = [3, 6]
# a2 = [i * 3 for i in a]
# print(a2)
#
# for e in a2:
#     print(e)
#
# a = 0
# while a < 10:
#     print a
#     a += 1  # due spazio per il commento
# else:
#     print "finito"

# a = ['stocazzo', 'had', 'a', 'little', 'lamb', 'mah']
# print (len(a))
# for i in range(len(a)):
#     print(i, a[i])

import boto3

s3client = boto3.client('s3')
response = s3client.list_buckets()
buckets: list = [bucket['Name'] for bucket in response['Buckets']]

# Print out the bucket list
print("Bucket List: %s" % buckets)

print(
    for bucket in buckets
        print("Bucket List: %s" % bucket)
)
