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
                is_user_in_group(user,g)
    return exist
parent = Group("parent")

child1 = Group("child1")

child2 = Group("child2")

child3 = Group("child3")

child4 = Group("child4")

subchild = Group("subchild")

subchild1 = Group("subchild1")

child1.add_user("jerome")

child2.add_user("sylvie")

child3.add_user("gregory")

child4.add_user("nicu")

subchild.add_user("sub_child_user")

subchild1.add_user("victoria")

child1.add_group(subchild)

child2.add_group(subchild1)

parent.add_group(child1)

parent.add_group(child2)

parent.add_group(child3)

parent.add_group(child4)

print ("Pass" if  (is_user_in_group(subchild, child1)) else "Fail")
print ("Pass" if  (is_user_in_group(child1, parent)) else "Fail")
print ("Pass" if  (is_user_in_group("jerome", child1)) else "Fail")
print ("Pass" if  (is_user_in_group("", child4)) else "Fail")
print ("Pass" if not (is_user_in_group(child4, parent)) else "Fail")

