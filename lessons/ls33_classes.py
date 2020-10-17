# Classes are a way to create our own data types.
# For example, a twitter profile

class TwitterProfile:
    handle: str
    followers: number = 0
    is_private: bool = True

# Initializing a ocmposite data type value rquires constructing a new object.

a_profile: TwitterProfile = TwitterProfile()
a_profile = TwitterProfile()

# Unlike built-in types, to establish an object with a custom type we must "construct" it
# We can use dot operator to look inside for attribue
print(a_profile.handle)
[object].[attribute]

# We can change attributes as well

aprofile.handle = "UNC"