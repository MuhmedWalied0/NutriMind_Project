import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:tester/auth/view/widgets/mainButton.dart';
import 'package:tester/auth/view/widgets/subheadtxt.dart';

import '../widgets/authtxtOfTextField.dart';
import '../widgets/donthave Account.dart';
import '../widgets/maintxt.dart';
import '../widgets/txtfield.dart';

class Signinscreen extends StatelessWidget {
  const Signinscreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('sign In',
        style: TextStyle(
          color:Colors.black,
          fontWeight: FontWeight.bold
        ),
        ),
        centerTitle: true,
        leading: BackButton(),
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 16.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              const Maintxt( txt:'Welcom Back!!',),
              const SizedBox(height: 12,),
              const Subheadtxt(txt: 'Good to see you again'),
              const SizedBox(height: 32,),
              const Authtxtoftextfield(txt: '  Email',),
              const CustomTextField(labelText: 'Enter Email', icona: Icons.email,),
              const SizedBox(height: 16,),
              const Authtxtoftextfield(txt: '  password',),
              const CustomTextField(labelText: 'Enter password', icona: Icons.password,),
              const SizedBox(height: 5,),
              Align(
                alignment: Alignment.bottomRight,
                child: TextButton(onPressed: (){},
                    child: const Text('forget passsword',
                    style: TextStyle(
                      color:Color(0xff1D6B44),
                      fontSize: 14,
                    ),
                    ),
                ),
              ),
              SizedBox(height: 48,),
              Mainbutton(func: (){}, txt: 'Sign In',),
              SizedBox(height: 8,),
              DontHaveAccount(),
              SizedBox(height: 64,),
              Image.asset('assets/or.png'),
              SizedBox(height: 32,),
              Image.asset('assets/google.png'),
            ],
          ),
        ),
      ),
    );
  }
}
