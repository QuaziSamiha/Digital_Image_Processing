olor(img, cv2.COLOR_BGR2GRAY)
# (n, m) = (grayImg.shape)
# i=0
# j=0
# k=0
# H = np.zeros((256), dtype=int)
# while k < 256:
#     H[k]=np.count_nonzero(grayImg==k)
#     k=k+1

# intensity = np.arange(0, 256, 1)
# # print(intensity)
# # print(H)
# plt.bar(intensity, H, color='maroon', width=0.5)
# plt.xlabel('intensity')
# plt.ylabel('frequency')
# plt.title('Histogram')
# plt.show()