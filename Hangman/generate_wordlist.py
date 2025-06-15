python_core = [
"print", "input", "type", "len", "int", "float", "str", "bool", "list", "tuple", "dict", "set", "if", "elif", "else", "for", "while", "break", "continue", "pass", "def", "return", "lambda", "try", "except", "raise", "finally", "assert", "with", "as", "import", "from", "class", "self", "in", "not", "is", "and", "or", "global", "nonlocal", "True", "False", "None", "range", "enumerate", "zip", "map", "filter", "reduce", "any", "all", "sorted", "reversed", "open", "read", "write", "append", "close", "join", "split", "strip", "format", "__init__", "__str__", "__repr__", "help", "dir", "id", "chr", "ord", "bin", "hex", "oct", "round", "pow",
]

data_structures = [
"array", "list", "tuple", "set", "dict", "stack", "queue", "linkedlist", "tree", "graph", "matrix", "node", "edge", "vertex", "hashmap", "hashset", "hashtable", "key", "value", "insert", "delete", "append", "remove", "pop", "sort", "reverse", "count", "index", "slice", "merge", "split", "zip", "enumerate", "pair", "flatten", "multidimensional", "binarytree", "preorder", "inorder", "postorder", "dfs", "bfs", "traversal", "heap", "priorityqueue", "minheap", "maxheap", "adjacency", "degree", "weight", "recursion", "depth", "level", "root", "leaf", "child", "parent", "sibling", "lookup", "reference", "pointer", "access", "size", "capacity", "search", "binarysearch", "linearsearch", "init", "class", "mutable", "immutable",
]

oop_concepts = [
"object", "class", "method", "attribute", "property", "constructor", "destructor", "inheritance", "encapsulation", "abstraction", "polymorphism", "interface", "override", "overload", "public", "private", "protected", "self", "init", "instance", "classmethod", "staticmethod", "super", "baseclass", "subclass", "hierarchy", "composition", "aggregation", "association", "ducktyping", "multipleinheritance", "singleton", "factory", "blueprint", "designpattern", "adapter", "observer", "decorator", "builder", "proxy", "encapsulate", "abstractclass", "virtualmethod", "typehint", "docstring", "module", "namespace", "metaclass", "initmethod", "getattr", "setattr", "isinstance", "issubclass", "objectoriented", "principle", "liskov", "cohesion", "coupling", "dependency", "solid", "principle", "diagram", "behavior", "modeling", "constructoroverloading", "reusability",
]

web_development = [
"html", "head", "body", "div", "span", "css", "color", "font", "margin", "padding", "flex", "grid", "position", "relative", "absolute", "zindex", "display", "inline", "block", "javascript", "dom", "event", "onclick", "onchange", "function", "variable", "const", "let", "array", "json", "parse", "stringify", "fetch", "ajax", "api", "post", "get", "put", "request", "response", "route", "endpoint", "server", "client", "cookie", "session", "localstorage", "form", "input", "label", "button", "nav", "link", "image", "src", "href", "class", "id", "tag", "element", "selector", "mediaquery", "transition", "transform", "animation", "keyframe", "layout", "responsive", "bootstrap",
]

git_devops = [
"git", "commit", "push", "pull", "branch", "merge", "rebase", "clone", "fork", "origin", "remote", "status", "diff", "log", "tag", "checkout", "stash", "conflict", "resolve", "version", "history", "repo", "repository", "init", "add", "ignore", "ci", "cd", "pipeline", "yaml", "runner", "trigger", "docker", "container", "image", "build", "deploy", "environment", "workflow", "hook", "automation", "rollback", "release", "kubernetes", "helm", "pod", "cluster", "service", "scale", "rollout", "ingress", "volume", "dockerfile", "dockerhub", "config", "secret", "registry", "token", "cipipeline", "devops", "jenkins", "githubactions", "terraform", "ansible", "provisioning", "infrastructure", "script", "configmap", "bash", "shell",
]

ai_ml_termsm = [
"dataset", "feature", "label", "model", "training", "testing", "validation", "accuracy", "precision", "recall", "f1score", "confusion", "matrix", "loss", "optimizer", "epoch", "batch", "gradient", "descent", "overfitting", "underfitting", "classification", "regression", "clustering", "decisiontree", "randomforest", "svm", "knn", "naivebayes", "neuralnet", "perceptron", "relu", "softmax", "sigmoid", "tanh", "backpropagation", "forwardpass", "weight", "bias", "layer", "dropout", "learningrate", "normalization", "scaling", "tokenization", "vectorization", "onehot", "embedding", "tfidf", "bagofwords", "transformer", "attention", "bert", "gpt", "train_test_split", "sklearn", "pandas", "numpy", "matplotlib", "seaborn", "keras", "tensorflow", "pytorch", "dataloader", "pipeline", "preprocessing", "augmentation", "tuning", "metrics",
]

linux_cli = [
"cd", "ls", "pwd", "mkdir", "rm", "rmdir", "cp", "mv", "touch", "nano", "vim", "cat", "less", "more", "head", "tail", "grep", "awk", "sed", "chmod", "chown", "sudo", "su", "ps", "kill", "top", "htop", "df", "du", "find", "locate", "tar", "zip", "unzip", "ping", "traceroute", "netstat", "ssh", "scp", "curl", "wget", "apt", "yum", "man", "history", "clear", "alias", "source", "bash", "zsh", "echo", "export", "env", "whoami", "uname", "hostname", "uptime", "cron", "crontab", "passwd", "useradd", "groupadd", "shutdown", "reboot", "mount", "unmount", "service", "systemctl"
]

all_words = python_core + data_structures + oop_concepts + web_development + git_devops + ai_ml_termsm + linux_cli

import random

random.shuffle(all_words)

with open("wordlist.txt", "w") as f:
    for word in all_words:
        f.write(word + "\n")
print("Word count:", len(all_words))
