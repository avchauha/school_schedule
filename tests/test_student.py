from school_schedule.student import Student


def test_instantiate_valid_student():
    quinn = Student(
                "Quinn", 
                "junior", 
                [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ]
            )

    assert quinn.name == "Quinn"
    assert len(quinn.classes) == 6

def test_get_num_classes_empty_list_returns_0():
    quinn = Student(
                "Quinn", 
                "junior", 
                []
            )
    
    result = quinn.get_num_classes()

    assert result == 0

def test_add_class_adds_class_to_list():
    # arrange
    quinn = Student(
                "Quinn", 
                "junior", 
                [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ]
            )    
    # act
    quinn.add_class("Underwater basket weaving")
    # assert
    assert len(quinn.classes) == 7
    assert "Underwater basket weaving" in quinn.classes