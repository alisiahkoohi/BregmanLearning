# train step
def train_step(conf, model, opt, train_loader):
    model.train()
    acc = 0
    loss = 0.0
    tot_steps = 0
    for batch_idx, (x, y) in enumerate(train_loader):
        # get batch data
        x, y = x.to(device), y.to(device)
        opt.zero_grad()
        logits = model(x)
        loss = conf.loss(logits, y)
        
        loss.backward()
        opt.step()
        acc += (logits.max(1)[1] == y).sum().item()
        loss += y.shape[0]*loss.item()
        tot_steps += y.shape[0]

    # print the current accuracy and loss
    if verbosity > 0: 
        print(50*"-")
        print('Train Accuracy:', acc/tot_steps)
        print('Train Loss:', loss)
    return {'loss':loss, 'acc':acc/tot_steps}




# validation step
def validation_step(conf, model, validation_loader, verbosity = 1):
    acc = 0.0
    loss = 0.0
    tot_steps = 0
    
    # -------------------------------------------------------------------------
    # loop over all batches
    for batch_idx, (x, y) in enumerate(validation_loader):
        # get batch data
        x, y = x.to(conf.device), y.to(conf.device)

        # update x to a adverserial example
        x = conf.attack(model, x, y)
        
         # evaluate model on batch
        logits = model(x)
        
        # Get classification loss
        c_loss = conf.loss(logits, y)
        
        acc += (logits.max(1)[1] == y).sum().item()
        loss += c_loss.item()
        tot_steps += y.shape[0]
        
    # print accuracy
    if verbosity > 0: 
        print(50*"-")
        print('Validation Accuracy:', acc/tot_steps)
    return {'loss':loss, 'acc':acc/tot_steps}




# test step
def test(model,test_loader):
    model.eval()
    acc = 0
    tot_steps = 0
    with torch.no_grad():
        for batch_idx, (x, y) in enumerate(test_loader):
            # get batch data
            x, y = x.to(device), y.to(device)
            # evaluate
            pred = model(x)
            acc += (pred.max(1)[1] == y).sum().item()
            tot_steps += y.shape[0]
    
    # print accuracy
    if verbosity > 0: 
        print(50*"-")
        print('Test Accuracy:', acc/tot_steps)
    return {'acc':acc/tot_steps}
