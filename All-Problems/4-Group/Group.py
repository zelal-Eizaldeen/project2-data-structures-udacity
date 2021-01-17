#Iterate through the dictionary
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name
    def compare(self,node, new_node):
      """
      0 means new_node equals node
      -1 means new node less than existing node
      1 means new node greater than existing node 
      """
      if new_node.get_value() == node.get_value():
          return 0
      elif new_node.get_value() < node.get_value():
          return -1
      else:
          return 1

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
Write a function that provides an efficient look up of whether the user is in a group.

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against

    """
    visited_groups = {}
    cur_group = group.groups
    exist = False
    if(user in group.users):
        exist = True
        return(exist)  
    
        
    else:
        for g in cur_group:
            if g.name in visited_groups:
                continue
            else:
                visited_groups[g.name] = g
                print(visited_groups,'here')
                is_user_in_group(user,g)
    return exist
