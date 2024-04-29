"Practica 5 IA-> Sistema de lógica de predicados en Python "

#clase para las reglas de inferencia
class Rule:
    def __init__(self, antecedent, consequent):
        self.antecedent = antecedent
        self.consequent = consequent

#clase para términos
class Term:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.name == other.name

    def __repr__(self):
        return self.name

#clase variables
class Variable(Term):
    pass

#clase constantes
class Constant(Term):
    pass

#clase para representar predicados
"se tienen nombre y aridad (número de argumentos)"
class Predicate:
    def __init__(self, name, arity):
        self.name = name
        self.arity = arity

    def __call__(self, *args):
        if len(args) != self.arity:
            raise ValueError(f"Predicate '{self.name}' expects {self.arity} arguments, got {len(args)}.")
        return (self.name,) + args

#clase para los cuantificadores 'para todo' y 'existe'
class Quantifier:
    def __init__(self, quantifier_type, variable, expression):
        self.quantifier_type = quantifier_type
        self.variable = variable
        self.expression = expression

#clase para representar la base del conocimiento
"contiene una lista de hechos representados como tuplas de la forma (predicado, argumento1,argumento2, ...)Esta base tiene métodos para agregar hechos y para consultar si un hecho en particular esta presente en ella"
class KnowledgeBase:
    def __init__(self):
        self.facts = []
        self.rules = []

    def add_fact(self, fact):
        self.facts.append(fact)

    def add_rule(self, rule):
        self.rules.append(rule)

    def query(self, predicate, *args):
        for fact in self.facts:
            if fact[0] == predicate.name and fact[1:] == args:
                return True
        return False

    def evaluate_rule(self, rule, facts):
        quantifier_type, variable, expression = rule.quantifier_type, rule.variable, rule.expression
        if quantifier_type == "forall":
            for fact in facts:
                if fact[0] == expression.name and fact[1] == variable.name:
                    return True
            return False
        elif quantifier_type == "exists":
            for fact in facts:
                if fact[0] == expression.name and fact[1] == variable.name:
                    return True
            return False
        else:
            raise ValueError("cuantificador no admitido")

#----------------------- menú principal ---------------------------
if __name__ == "__main__":
    #crear algunos predicados
    likes = Predicate("likes", 2)
    rich = Predicate("rich", 1)
    happy = Predicate("happy", 1)

    #crear la base de conocimiento 
    kb = KnowledgeBase()

    #agregar algunos hechos
    kb.add_fact(likes("Alice", "Bob"))
    kb.add_fact(rich("Bob"))
    kb.add_fact(happy("Alice"))

    #realizar algunas consultas
    print("\nConsultas--------------------------------------")
    print(kb.query(likes, "Alice", "Bob")) #true
    print(kb.query(likes, "Bob", "Alice")) #false
    print(kb.query(rich, "Bob")) #true
    print(kb.query(happy, "Alice")) #true
    print(kb.query(happy, "Bob")) #false

    #regla con cuantificador 'forall' (para todo)
    rich_variable = Variable("x") 
    happy_variable = Variable("x")
    forall_rule = Quantifier("forall", rich_variable, Predicate("rich", 1))
    forall_rule.expression = Predicate("happy", 1)

    #agregar la regla ala base de conocimiento
    kb.add_rule(forall_rule)

    #evaluar la regla agregada 'para todo'
    print("\ncuantificador forall--------------------------------------")
    if kb.evaluate_rule(forall_rule, kb.facts):
        print("Para todos los ricos, hay felicidad")
    else:
        print("No se puede inferir la relación entre riqueza y felicidad para todos los casos")

    # crear un cuantificador 'exists'
    exists_rule = Quantifier("exists", rich_variable, Predicate("rich", 1))

    # agregar la regla a la base de conocimiento
    kb.add_rule(exists_rule)

    # Evaluar la regla
    print("\nCuantificador exists--------------------------------------")
    if kb.evaluate_rule(exists_rule, kb.facts):
        print("Existe al menos un individuo rico")
    else:
        print("No se puede inferir la existencia de individuos ricos")
    
    # instancias de reglas de inferencia (2)
    "1.-Modus Ponens: si tenemos una proposición condicional del tipo si p, entonces q (p -> q), sabemos que p es verdadera, entonces podemos inferir que  q también "
    modus_ponens_rule = Rule((likes("Alice", "Bob"), rich("Bob")), happy("Alice"))
    "2.-Silogismo Hipotético: si tenemos dos proposiciones condicionales como si p, entonces q (p -> q) y si q, entonces r (q -> r), podemos inferir la conclusión r si la premisa p es verdadera"
    silogismo_hipotetico_rule = Rule((likes("Alice", "Bob"), rich("Bob")), (rich("Bob"), happy("Alice")))

    # agregar reglas instancias a la base de conocimiento
    kb.add_rule(modus_ponens_rule)
    kb.add_rule(silogismo_hipotetico_rule)

    # comrprobar la regla de INFERENCIA Modus Ponens 
    print("\nInferencia 1. Modus ponens--------------------------------------")
    if kb.query(likes, "Alice", "Bob") and kb.query(rich, "Bob"):
        print("La regla Modus Ponens se cumple:")
        print("Si a Alice le gusta Bob y Bob es rico, entonces Alice es feliz")
        print("Alice es feliz")

    # comprobar la regla de INFERENCIA Silogismo hipotetico
    print("\nInferencia 2. silogismo hipotetico------------------------------")
    if kb.query(likes, "Alice", "Bob") and kb.query(rich, "Bob"):
        print("\nLa regla Silogismo Hipotético se cumple:")
        print("Si a Alice le gusta Bob y Bob es rico, entonces Bob es feliz")
        print("Bob es feliz")

