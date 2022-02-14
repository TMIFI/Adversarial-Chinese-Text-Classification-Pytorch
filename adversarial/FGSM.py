#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import torch

class Adv():
    def __init__(self, model):
        self.model = model
        self.backup = {}
        self.name = "FGSM"

    def attack(self, epsilon=1., emb_name='embedding.'):
        # emb_name这个参数要换成你模型中embedding的参数名
        for name, param in self.model.named_parameters():
            if param.requires_grad and emb_name in name:
                self.backup[name] = param.data.clone()
                r_at = epsilon * torch.sign(param.grad)
                param.data.add_(r_at)

    def restore(self, emb_name='embedding.'):
        # emb_name这个参数要换成你模型中embedding的参数名
        for name, param in self.model.named_parameters():
            if param.requires_grad and emb_name in name: 
                assert name in self.backup
                param.data = self.backup[name]
        self.backup = {}
