from tkinter import *
from tkinter import ttk
import copy
import dill
import pickle
import os

lastx, lasty = 0, 0		
previous_object=-1		
previous_polygon=-1			
color = "black"				
figure = "freehand"			
polygon = []				
mode = "draw"				
select_mode = "move"	
selection_id = -1		
clipboard_info=[]		
advanced_mode="group"		
group_elements=[]			
counter_obj={"group":0,"freehand":0,"polygon":0}
debugOutput=False

def sign(number):
	if number>0:
		return 1;
	elif number<0:
		return -1;
	else:
		return 0;
def delObject(toDelete):									
	if toDelete != -1:
		canvas.delete(toDelete)
def findNearest(event):
	default_id = canvas.find_closest(event.x, event.y)[0]
	selection_tags = canvas.gettags(default_id)
	for tag in selection_tags:									
		if tag.find("button") != -1:						
			return -1										
	for tag in selection_tags:									
		if tag.find("group") != -1:								
			return tag											
	for tag in selection_tags:									
		if (tag.find("free")!=-1) or (tag.find("poly")!=-1):	
			return tag											
	return default_id										
def tagsBeforeGroup(identifier):
	allTags = canvas.gettags(identifier)
	returnTags=[]
	for j in allTags:
		if j.find("group")==-1:								
			returnTags.append(j)								
	return returnTags											
def getNewTag(tag):
	global counter_obj
	tagType,suffix=tag.split('_')
	counter_obj[tagType]=counter_obj[tagType]+1
	newTag=tagType+"_"+str(counter_obj[tagType])
	return newTag
def setColor(newcolor):
    global color
    color = newcolor
    print("Color: "+color)
def setFigure(newfigure):
	global figure, mode
	figure=newfigure
	mode="draw"
	print("Mode: Draw ; Figure: "+figure)
def setSelection(newMode):
	global figure, mode, select_mode, selection_id
	mode="select"
	select_mode = newMode
	selection_id = -1
	print("Mode: Select ; Option: "+select_mode)

def setAdvanced(newMode):
	global figure, mode, advanced_mode, selection_id, group_elements
	mode="advanced"
	group_elements = []
	advanced_mode = newMode
	selection_id = -1
	print("Mode: Advanced ; Option: "+advanced_mode)
def setSaved(option):
	if option == "save":
		saveToDisk()
		print("Saving to disk")
	elif option == "load":
		loadFromDisk()
		print("Loading from disk")
	else:
		print("ERROR: INVALID ELSE 6")
def addFree(event):												
    global lastx, lasty, counter_obj
    prefix='freehand_'
    canvas.create_line((lastx, lasty, event.x, event.y), fill=color, tags=(prefix+str(counter_obj["freehand"])))
    lastx, lasty = event.x, event.y
    return prefix+str(counter_obj["freehand"])
def addStraight(event):
    global lastx, lasty, previous_object
    delObject(previous_object)
    previous_object = canvas.create_line((lastx, lasty, event.x, event.y), fill=color)
def addEllipse(event):
    global lastx, lasty, previous_object
    delObject(previous_object)
    previous_object = canvas.create_oval((lastx, lasty, event.x, event.y), fill=color)
def addRectangle(event):
    global lastx, lasty, previous_object
    delObject(previous_object)
    previous_object = canvas.create_rectangle((lastx, lasty, event.x, event.y), fill=color)
def addSquare(event):
    global lastx, lasty, previous_object
    delObject(previous_object)
    square_dim = min(abs(event.x-lastx), abs(event.y-lasty))	
    newx = lastx + (square_dim*sign(event.x-lastx))
    newy = lasty + (square_dim*sign(event.y-lasty))
    previous_object = canvas.create_rectangle((lastx, lasty, newx, newy), fill=color)
def addCircle(event):
    global lastx, lasty, previous_object
    delObject(previous_object)
    circle_dim = min(abs(event.x-lastx), abs(event.y-lasty))	
    newx = lastx + (circle_dim*sign(event.x-lastx))
    newy = lasty + (circle_dim*sign(event.y-lasty))
    previous_object = canvas.create_oval((lastx, lasty, newx, newy), fill=color)
def addPolygon(event):							
    global lastx, lasty, previous_object
    delObject(previous_object)
    previous_object = canvas.create_line((lastx, lasty, event.x, event.y), fill=color, width=2)

def drawPolygon(polygondata, outline, width):			
	global counter_obj
	canvas.delete(previous_object)
	prefix='polygon_'
	counter_obj["polygon"] = counter_obj["polygon"]+1
	for i in range(len(polygondata)-1):
		id = canvas.create_line(polygondata[i],polygondata[i+1], width=width, fill=outline, tags=(prefix+str(counter_obj["polygon"])))
	return prefix+str(counter_obj["polygon"])
def cleanPolygon(polygondata, options):				
	global counter_obj
	prefix='polygon_'
	counter_obj["polygon"] = counter_obj["polygon"]+1
	for i in polygondata:
		id = canvas.create_line(i)
		canvas.itemconfigure(id, options)
		canvas.dtag(id)
		canvas.itemconfig(id, tags=(prefix+str(counter_obj["polygon"])))
	return prefix+str(counter_obj["polygon"])
def selectOptions(event):
	global selection_id, lastx, lasty
	if select_mode == "cut":
		retainObjectInfo(event)
		canvas.delete(selection_id)
	elif select_mode == "copy":
		retainObjectInfo(event)
	elif select_mode == "move":
		lastx, lasty = event.x, event.y
	elif select_mode == "paste":
		pass
	else:
		print("ERROR:WRONG MODE DETECTED 5")
def moveStuff(event):
	global lastx, lasty
	if selection_id != -1:								
		xAmount = event.x-lastx
		yAmount = event.y-lasty
		canvas.move(selection_id, xAmount, yAmount)
		lastx, lasty = event.x, event.y
def retainObjectInfo(event):
	global selection_id, clipboard_info
	clipboard_info=[]										
	for drawing_id in canvas.find_withtag(selection_id):	
		drawing_info={}									
		drawing_info["options"]={}
		drawing_info["type"]=canvas.type(drawing_id)
		drawing_info["options"]["width"]=canvas.itemcget(drawing_id, "width")
		drawing_info["options"]["fill"]=canvas.itemcget(drawing_id, "fill")
		drawing_info["options"]["tags"]=canvas.itemcget(drawing_id, "tags")
		drawing_info["coords"]=canvas.coords(drawing_id)
		clipboard_info.append(drawing_info)					
	if debugOutput:
		print(clipboard_info)
		
def renderClipboard(event):
	global clipboard_info
	function_list={
		"freehand":cleanPolygon, 
		"line":getattr(canvas,"create_line"),
		"rectangle":getattr(canvas,"create_rectangle"),
		"oval":getattr(canvas,"create_oval"),
		"polygon":cleanPolygon
	}
	tags_seen={}
	clip=copy.deepcopy(clipboard_info)
	if not clip:												
		return														
	xDiff=event.x-clip[0]["coords"][0]
	yDiff=event.y-clip[0]["coords"][1]
	for drawing in clip:
		drawing["coords"][0]=drawing["coords"][0]+xDiff
		drawing["coords"][2]=drawing["coords"][2]+xDiff
		drawing["coords"][1]=drawing["coords"][1]+yDiff
		drawing["coords"][3]=drawing["coords"][3]+yDiff
		if drawing["options"]["tags"]!='':									
			old_tags = drawing["options"]["tags"].split(" ")			
			new_tags=[]
			for curr_tag in old_tags:
				if curr_tag not in ("{}","current"):					
					if curr_tag not in tags_seen:							
						tags_seen[curr_tag]=getNewTag(curr_tag)				
					new_tags.append(tags_seen[curr_tag])					
			drawing["options"]["tags"] = new_tags
		function_list[drawing["type"]](drawing["coords"], drawing["options"])
def advancedOptions(event):
	global advanced_mode, lastx, lasty, selection_id, group_elements
	if advanced_mode == "group":
		selection_id = findNearest(event)
		if selection_id!=-1:
			group_elements.append(selection_id)
	elif advanced_mode == "ungroup":
		selection_id = findNearest(event)
		ungroupElements(event)
	else:
		print("ERROR:WRONG MODE DETECTED 1")
def groupElements(event):
	global counter_obj
	prefix="group_"
	counter_obj["group"] = counter_obj["group"] + 1
	for i in group_elements:
		canvas.itemconfig(i, tags=(prefix+str(counter_obj["group"]),canvas.gettags(i)))
	print("Group created: "+prefix+str(counter_obj["group"]))
def ungroupElements(event):
	global selection_id
	if type(selection_id)==int:
		return
	if selection_id.find("group")!=-1:						
		for i in canvas.find_withtag(selection_id):			
			canvas.itemconfig(i, tags=tagsBeforeGroup(i))	
	print("Group ungrouped: "+selection_id)
def saveToDisk(): 										
	save_object={}
	save_object["counter_obj"]=counter_obj
	save_object["objects"]=[]
	
	items = canvas.find_all()
	for curr_item in items:
		tags_list=canvas.itemcget(curr_item, "tags").split(" ")
		flag=False
		for curr_tag in tags_list:					
			if curr_tag.find("buttons")!=-1:
				flag=True
		if not flag:									
			item_info={}								
			item_info["options"]={}
			item_info["type"]=canvas.type(curr_item)
			item_info["options"]["width"]=canvas.itemcget(curr_item, "width")
			item_info["options"]["fill"]=canvas.itemcget(curr_item, "fill")
			item_info["options"]["tags"]=tags_list
			item_info["coords"]=canvas.coords(curr_item)
			save_object["objects"].append(item_info)	#append item data to saving object
	if(debugOutput):		
		print(save_object)
	file_name=entry1.get()
	if file_name=='':
		print("No filename input, returning without saving")
		return
	with open(file_name, 'wb') as datafile:
		pickle.dump(save_object, datafile)
def loadFromDisk(): 								
	file_name=entry1.get()
	if file_name=='':
		print("No filename input, returning without loading")
	if os.path.isfile(file_name):
		with open(file_name, 'rb') as datafile:
			save_object = pickle.load(datafile)
	else:
		print("NO SAVE FILE FOUND")
		return
	if debugOutput:
		print(save_object)
	delAllExceptButtons()								
	counter_obj=save_object["counter_obj"]
	renderSaveData(save_object)					
def delAllExceptButtons():							
	print("Clearing screen")
	items = canvas.find_all()
	for curr_item in items:
		tags_list=canvas.itemcget(curr_item, "tags").split(" ")
		flag=False
		for curr_tag in tags_list:						
			if curr_tag.find("buttons")!=-1:
				flag=True
		if not flag:								
			canvas.delete(curr_item)
def renderSaveData(save_object):					
	function_list={
		"freehand":cleanPolygon, 
		"line":getattr(canvas,"create_line"),
		"rectangle":getattr(canvas,"create_rectangle"),
		"oval":getattr(canvas,"create_oval"),
		"polygon":cleanPolygon
	}
	for drawing in save_object["objects"]:
		function_list[drawing["type"]](drawing["coords"], drawing["options"])
def left_click(event):
    global lastx, lasty, previous_object, polygon, previous_polygon, counter_obj, selection_id
    if mode == "draw":
        lastx, lasty = event.x, event.y
        previous_object=-1
        polygon=[]
        polygon.append((event.x,event.y))
        previous_polygon=-1
        if figure=="freehand":
            counter_obj["freehand"] = counter_obj["freehand"] + 1
    elif mode == "select":
        selection_id = findNearest(event)
        print(selection_id)
        if (selection_id!=-1):		
            selectOptions(event)
    elif mode == "advanced":
        selection_id = findNearest(event)
        print(selection_id)
        if (selection_id!=-1):
            advancedOptions(event)
    else:
        print("ERROR:WRONG MODE DETECTED IN <left_click>")
def right_click(event):
	global lastx, lasty, previous_object, previous_polygon, polygon
	if mode=="draw":
		if figure == "polygon":
			delObject(previous_polygon)
			polygon.append((event.x,event.y))
			previous_polygon = drawPolygon(polygon, outline=color, width=2)
			lastx = event.x
			lasty = event.y
	elif mode=="select":
		if select_mode=="paste":
			renderClipboard(event)
	elif mode=="advanced":
		groupElements(event)
	else:
		print("ERROR:WRONG MODE DETECTED IN <right_click>")
def mouse_move(event):
	if mode=="draw": 
		if figure=="freehand":
			addFree(event);
		elif figure=="straight":
			addStraight(event);
		elif figure=="rectangle":
			addRectangle(event);
		elif figure=="ellipse":
			addEllipse(event);
		elif figure=="square":
			addSquare(event);
		elif figure=="circle":
			addCircle(event);
		elif figure=="polygon":
			addPolygon(event);
		else:
			print("ERROR IN CHOICE, CHECK CODE 2")
	elif mode=="select":
		if select_mode=="move":
			moveStuff(event)
		elif select_mode=="cut":
			print("cut")
		elif select_mode=="copy":
			print("copy")
		elif select_mode=="paste":
			print("paste")
		else:
			print("ERROR IN CHOICE, CHECK CODE 3")
	elif mode=="advanced":
		print("click drag in advanced mode detected")
	else:
		print("ERROR IN CHOICE, CHECK CODE 4")
	canvas.tag_raise("buttons")
root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
canvas = Canvas(root)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))
canvas.bind("<Button-1>", left_click)
canvas.bind("<B1-Motion>", mouse_move)
canvas.bind("<Button-2>", right_click)
canvas.bind("<Button-3>", right_click)
avail_colors=["black", "red", "green", "blue", "cyan", "yellow", "magenta","white"]
counter=10
def color_lambda(var):
	return lambda x: setColor(var)
for curr in avail_colors:
	id = canvas.create_rectangle((10, counter, 30, counter+20), fill=curr, tags=('buttons'))
	canvas.tag_bind(id, "<Button-1>", color_lambda(curr))
	counter = counter + 25;
avail_figures=["freehand", "straight", "rectangle", "ellipse", "square", "circle", "polygon"]
counter=35
def figure_lambda(var):
	return lambda x: setFigure(var)
for curr in avail_figures:
	id = canvas.create_rectangle((counter, 10, counter+70, 30), fill="white", tags=('buttons'))
	canvas.tag_bind(id, "<Button-1>", figure_lambda(curr))
	id = canvas.create_text((counter+5, 10), text=curr, tags=('buttons'), anchor=NW)
	canvas.tag_bind(id, "<Button-1>", figure_lambda(curr))
	counter = counter + 75;
selection_options=["move", "cut", "copy", "paste"]
def selection_lambda(var):
	return lambda x: setSelection(var)
for curr in selection_options:
	id = canvas.create_rectangle((counter, 10, counter+70, 30), fill="black", tags=('buttons'))
	canvas.tag_bind(id, "<Button-1>", selection_lambda(curr))
	id = canvas.create_text((counter+5, 10), text=curr, tags=('buttons'), anchor=NW, fill="white")
	canvas.tag_bind(id, "<Button-1>", selection_lambda(curr))
	counter = counter + 75;
advanced_options=["group", "ungroup"]
def advanced_lambda(var):
	return lambda x: setAdvanced(var)
for curr in advanced_options:
	id = canvas.create_rectangle((counter, 10, counter+70, 30), fill="white", tags=('buttons'))
	canvas.tag_bind(id, "<Button-1>", advanced_lambda(curr))
	id = canvas.create_text((counter+5, 10), text=curr, tags=('buttons'), anchor=NW)
	canvas.tag_bind(id, "<Button-1>", advanced_lambda(curr))
	counter = counter + 75;

entry1 = Entry (root) 
canvas.create_window(counter, 10, window=entry1, anchor=NW, tags=('buttons'))
counter = counter + 170;
saving_options=["save", "load"]
def saving_lambda(var):
	return lambda x: setSaved(var)
for curr in saving_options:
	id = canvas.create_rectangle((counter, 10, counter+70, 30), fill="black", tags=('buttons'))
	canvas.tag_bind(id, "<Button-1>", saving_lambda(curr))
	id = canvas.create_text((counter+5, 10), text=curr, tags=('buttons'), anchor=NW, fill="white")
	canvas.tag_bind(id, "<Button-1>", saving_lambda(curr))
	counter = counter + 75;



root.mainloop()
