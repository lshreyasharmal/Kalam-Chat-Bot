import pickle
def preprocess(data):
	scenes = {}
	for line in data:
		scene_id = line.split("\t")[1]
		dialogue = line.split("\t")[4]
		if scene_id not in scenes.keys():
			scenes[scene_id] = []
			scenes[scene_id].append(dialogue)
		else:
			scenes[scene_id].append(dialogue)
	return scenes
	
friends_final = open("/home/mypc/Desktop/7th Sem/NLP/Project/Data-20180920T174835Z-001/Data/friends-final.txt")
raw_data = friends_final.readlines()
scenes = preprocess(raw_data)
with open("dataset.pkl","wb") as data:
	pickle.dump(scenes,data)
