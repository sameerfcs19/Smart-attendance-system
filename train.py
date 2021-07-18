import cognitive_face as CF
from global_variables import personGroupId

Key = '339187af77ca4813ab3de6a86817916b'
CF.Key.set(Key)

BASE_URL = 'https://southeastasia.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

res = CF.person_group.train(personGroupId)
print(res)
