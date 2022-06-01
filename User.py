class User:
    user_post_dict = {}
    user_post_list =[]

    def __init__(self, name, email, drivers):
        self.name = name
        self.email = email
        self.drivers = drivers
        self.post = []
    def __str__(self):
        return (f"Welcome {self.name}")
    
    def user_post(self, post):
        self.post.append(post)
        User.user_post_dict[self.name] = self.post
        User.user_post_list.append(f"{self.name} : {self.post}")

       
    def post_delete(self):
        self.post.pop(-1)
        User.user_post_list.pop(-1)

	   
		
			
	
    
dennis = User("dennis", "dennis.corral@outlook.com", "D9285176")
diego = User("diego", "diego.corral@gmail.com", "D123456")
bella = User("bella", "bella.corral@usmc.mil", "B234234")

dennis.user_post('hi')
bella.user_post('sup')
dennis.user_post('delete this')
dennis.user_post('good afternoon')
dennis.user_post(' =/ ')
dennis.post_delete()

print(dennis.post)
print(User.user_post_dict)
print(User.user_post_list)


# print(dennis)