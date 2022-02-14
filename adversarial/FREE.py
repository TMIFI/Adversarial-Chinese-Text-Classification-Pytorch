#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import torch

class Adv():
    def __init__(self, model):
        self.model = model
        self.emb_backup = {}
        self.name = "FREE"
        self.backup()

    def attack(self, epsilon=1., emb_name='embedding.'):
        # emb_name这个参数要换成你模型中embedding的参数名
        for name, param in self.model.named_parameters():
            if param.requires_grad and emb_name in name:
                r_at = epsilon * torch.sign(param.grad)
                param.data.add_(r_at)
                param.data = self.project(name, param.data, epsilon)

    def project(self, param_name, param_data, epsilon):
        r = param_data - self.emb_backup[param_name]
        if torch.norm(r) > epsilon:
            r = epsilon * r / torch.norm(r)
        return self.emb_backup[param_name] + r
    
    def backup(self, emb_name='embedding.'):
        for name, param in self.model.named_parameters():
            if param.requires_grad and emb_name in name:
                self.emb_backup[name] = param.data.clone()

