from unicodedata import name
from django.urls import path
from shop import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm,MySetPasswordForm

urlpatterns = [
    path('',views.ProductView.as_view(), name="home"),

    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    # path('', views.home),
    # path('product-detail/', views.product_detail, name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/',views.show_cart, name='showcart'),
    path('pluscart/',views.plus_cart),
    path('minuscart/',views.minus_cart),
    path('removecart/', views.remove_cart),
    
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    # path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('laptop/',views.laptop, name= 'laptop'),
    path('laptop/<slug:dat>', views.laptop, name= 'laptopdata'),

    # path('login/', views.login, name='login'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm),name = 'login'),
    # path('registration/', views.customerregistration, name='customerregistration'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name = 'logout'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view
    (template_name='passwordchange.html',form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), 
    name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeView.as_view
    (template_name='passwordchangedone.html'), name='passwordchangedone'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),


    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
]
