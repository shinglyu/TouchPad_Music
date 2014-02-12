import pygame.midi

pygame.midi.init()
print("There are " + str(pygame.midi.get_count()) + " midi devices")
print("The default is port " + str(pygame.midi.get_default_input_id()))

for did in range(0,pygame.midi.get_count()):
   print("Device No. " + str(did))
   print(pygame.midi.get_device_info(did))


#src = pygame.midi.Input(pygame.midi.get_default_input_id())
src = pygame.midi.Input(8)
while(True):
   #print(src.poll())
   if(src.poll()):
      print(src.read(1))

