class Taxi:  
  def __init__(self, id, dest, pos_dest, pos_actual, path=None):
    self.id = id
    self.dest = dest
    self.pos = pos_actual    
    self.pos_dest = pos_dest
    self.path = path
    self.ocupado = 'si'
    

