#Eclipse Phase Data 
This repository lists the traits, skills, aptitudes and other associated gameplay stats for the tabletop roleplaying game Eclipse Phase

##**skills.yaml**

--------------------------------------------------------------------------

Aptitudes:
  - Name of aptitude
  
  ...
  

Skills:
  - Name of Skills : Governing Aptitude
  
  ...

--------------------------------------------------------------------------

##**traits.yaml**

--------------------------------------------------------------------------

Name of Trait:
  - Cost: (CP cost or bonus)
  - Type: (Positive, Negative or Neutral)
  - EoM: (Ego or Morph, or Both)
  - Description: (Text from books)
  - Restriction: (Limited to particular morph, faction, background etc)
  - Dependency: (Dependant on other traits, IE Adapatability Level 2 has dependency on Adaptability level 1)
  
  ...
  
For traits with multiple levels, each level has been created as a seperate trait with indicated dependancy. CP cost of traits with levels is listed as the price to increase from the previous level. IE Adaptability Level 1 costs 10 points and is a dependancy for Level 2, since Level 2 costs 20 CP total, it is listed as 20-10 = 10 CP (Total - Already paid).

--------------------------------------------------------------------------

##**Planned**

**morphs.yaml**
  - Implants:
    - List of implants
  - Movement Rate:
    - Movement type: (Normal/Run)
    - ...
  - Aptitude Maximum:
    - Aptitude: Max Value
    - ...
  - Durability: Value
  - Wound Threshold: Value
  - Advantages:
    - Skill or aptitude: Bonus
    - ...
  - Disadvantages:
    - Skill or aptitude: Negative Bonus
    - ...
  - Notes : Other things to note
  - CP: Cost
  - Credit: Cost
  - Speed Modifier: Value
  - Description: Text from books
