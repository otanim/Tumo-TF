import tensorflow as tf
#1
tf.constant("Hello World", dtype=None, name="Const")

a = tf.constant(5.0)
b = tf.constant(6.0)
c = a * b

# sess = tf.Session()
# print(sess.run(c))
# sess.close()

with tf.Session() as sess:
    print(sess.run(c))

#2
x = tf.constant(2, dtype=None, name="Const")
y = tf.constant(3, dtype=None, name="Const")
z = x * y
tf_z = tf.multiply(x, y)

with tf.Session() as sess:
    print(sess.run(x))
    print(sess.run(y))
    print(sess.run(z))
    print(sess.run(tf_z))