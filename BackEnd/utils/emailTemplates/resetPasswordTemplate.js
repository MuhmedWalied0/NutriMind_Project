export const resetPasswordTemplate = (token) => `
<body style="
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%);
    margin: 0;
    padding: 20px;
    min-height: 100vh;
">
    <div style="
        background: linear-gradient(145deg, #1e1e1e 0%, #2a2a2a 100%);
        border: 1px solid #333;
        border-radius: 20px;
        padding: 40px;
        max-width: 500px;
        margin: 0 auto;
        box-shadow: 
            0 20px 40px rgba(0, 0, 0, 0.5),
            0 0 0 1px rgba(255, 255, 255, 0.05);
        position: relative;
        overflow: hidden;
    ">
        <!-- Top gradient line -->
        <div style="
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 2px;
            background: linear-gradient(90deg, #4caf50, #81c784, #4caf50);
        "></div>
        
        <!-- Header -->
        <div style="text-align: center; margin-bottom: 30px;">
            <h2 style="
                color: #f5f5f5;
                font-size: 28px;
                font-weight: 600;
                margin-bottom: 10px;
                text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
            ">NutriMind</h2>
            
            <div style="
                color: #4caf50;
                font-size: 16px;
                font-weight: 500;
                opacity: 0.9;
            ">Password Reset Request</div>
        </div>
        
        <!-- Content -->
        <div style="text-align: center; margin: 30px 0;">
            <p style="
                color: #e0e0e0;
                font-size: 16px;
                line-height: 1.6;
                margin-bottom: 25px;
            ">Your password reset verification code is:</p>
            
            <!-- Token Container -->
            <div style="
                background: linear-gradient(135deg, #2d2d2d, #3a3a3a);
                border: 2px solid #4caf50;
                border-radius: 15px;
                padding: 20px;
                margin: 25px 0;
                position: relative;
                box-shadow: 
                    0 8px 25px rgba(76, 175, 80, 0.2),
                    inset 0 1px 0 rgba(255, 255, 255, 0.1);
            ">
                <div style="
                    color: #4caf50;
                    font-size: 14px;
                    font-weight: 600;
                    text-transform: uppercase;
                    letter-spacing: 1px;
                    margin-bottom: 10px;
                ">Verification Code</div>
                
                <div style="
                    color: #ffffff;
                    font-size: 32px;
                    font-weight: 700;
                    font-family: 'Courier New', monospace;
                    letter-spacing: 3px;
                    text-shadow: 0 2px 8px rgba(76, 175, 80, 0.3);
                    margin-bottom: 10px;
                ">${token}</div>
                
                <div style="
                    color: #ff9800;
                    font-size: 14px;
                    font-weight: 500;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    gap: 8px;
                ">⏰ Expires in 10 minutes</div>
            </div>
            
            <!-- Security Note -->
            <div style="
                background: rgba(255, 152, 0, 0.1);
                border: 1px solid rgba(255, 152, 0, 0.3);
                border-radius: 10px;
                padding: 15px;
                margin: 20px 0;
                color: #ffb74d;
                font-size: 13px;
                display: flex;
                align-items: center;
                gap: 10px;
            ">
                🔒 <span>Please enter this code in the application to reset your password</span>
            </div>
        </div>
        
        <!-- Footer -->
        <div style="
            text-align: center;
            color: #888;
            font-size: 14px;
            line-height: 1.5;
        ">
            <p style="margin-bottom: 5px;"><strong>Didn't request this action?</strong></p>
            <p style="margin: 0;">You can safely ignore this email. Nothing will be changed in your account.</p>
        </div>
    </div>
</body>
`;
