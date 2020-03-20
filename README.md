# CS419MachineLearning
TEAM D.E.C.K.T.M. - Designing Everything Creatively, Kindly, Tremendously Magnificent

ML SECURITY
• A platform for adversarial attack and defenses
• Administrator can publish datasets to users to train models
• MNIST, CIFAR-10
• Users train robust models
• Users submit adversarial examples to attack all others’ models
• A leaderboard GUI is required to show the accuracy of each model and attack
success rate
• You can use existing implementations of many attacks/defenses, but one attack
and one defense have to be your own implementation

MINIMAL
• Built-in datasets, MNIST and CIFAR
• Built-in models (at least one for each dataset)
• Up-to-date leaderboard
• At least one attack algorithm and one defense

ATTACK MODES
White-box
• Administrator publishes the model, users can also publish models
• Users attack it with full control
• Black-box
• Administrator publishes the dataset only
• Users attack each other’s model (Adversarial examples transfer!)
• Gray-box
• Administrator publishes the model with constraints
• # query or frequency, output label or result vector
• Administrators configure these modes and also choose these options

USER
Users can perform attacks
• Submit attack images
• Submit attack algorithm
• Users can train robust models
• Submit the trained models
• The system can
• Automatically attack published/submitted models using submitted attack
images/algorithms
• Update the leaderboard

PROJECT OVERALL
Artifacts
• Code
• Documentation including dependencies, compilation instructions and
parameters, inputs to program etc.
• A report including your detailed design, evaluation
• Presentation in the last week!
• Live demo is required.


