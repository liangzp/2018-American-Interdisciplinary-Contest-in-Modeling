from pylab import *
X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)


plot(X,-X,color='k')
xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$very \quad insensitive$', r'$insensitive$', r'$neutral$', r'$sensitive$', r'$very \quad sensitive$'])

yticks([-np.pi, -np.pi/2, np.pi/2, np.pi],
       [r'$very \quad insensitive$', r'$insensitive$', r'$sensitive$', r'$very \quad sensitive$'])
#xlabel('potential owners sensitivity')
#ylabel('current owners sensitivity')
#plot(X,S)
ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
show()