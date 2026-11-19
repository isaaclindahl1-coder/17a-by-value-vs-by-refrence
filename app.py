#Primitive types: int, str, bool, float, dict?


def primitive_int(val:int):
    val += 1

def primitive_str(val:str):
    val += 1

def primitive_bool(val:bool):
    val = not val

def primitive_float(val:float):
    val += 1

#dictionary - NOT primitive - a complex type, PASSED BY REFRENCE
def not_primitive_dict(val:dict):
    val["updated"] = True

#list not primitive

def main():
    my_int = 1 
    primitive_int(my_int)
    print(f"My int was 1, after function it is {my_int}")
    my_str = "HEllo"
    primitive_str(my_str)
    print(f"My int was \"Hello\", after function it is {my_str}")
    my_bool = True 
    primitive_bool(my_bool)
    print(f"My int was True, after function it is {my_bool}")
    my_float = 1.1 
    primitive_float(my_float)
    print(f"My float was 1.1, after function it is {my_float}")
    my_dict = {"updated": False} 
    primitive_dict(my_dict)
    print(f"My int was {{\"updated\": False}}, after function it is {my_dict}")

if __name__ == "__main__":
    main()