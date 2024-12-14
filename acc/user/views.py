from django.shortcuts import render, redirect
from .forms import CustomUserRegistrationForm
from .models import CustomUser, UserCriteriaLink
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from collections import defaultdict
from django.contrib.auth.decorators import login_required

CRITERIA_LIST = {
    '1_1_1': "Criteria 1.1.1",
    '1_2_2': "Criteria 1.2.2",
    '1_3_1': "Criteria 1.3.1",
    '1_3_2': "Criteria 1.3.2",

    # criteria 2
    '2_3_1': "Criteria 2.3.1",
    '2_4_2': "Criteria 2.4.2",
    '2_5_1': "Criteria 2.5.1",
    '2_6_1': "Criteria 2.6.1",
    '2_6_2': "Criteria 2.6.2",
    '2_6_3': "Criteria 2.6.3",
    '2_7_1': "Criteria 2.7.1",

    # criteria 3
    '3_1_1': "Criteria 3.1.1",
    '3_2_1': "Criteria 3.2.1",
    '3_2_2': "Criteria 3.2.2",
    '3_3_1': "Criteria 3.3.1",
    '3_3_2': "Criteria 3.3.2",
    '3_4_1': "Criteria 3.4.1",
    '3_4_2': "Criteria 3.4.2",
    '3_4_3': "Criteria 3.4.3",
    '3_5_1': "Criteria 3.5.1",

    # criteria 4
    '4_1_1': "Criteria 4.1.1",
    '4_1_2': "Criteria 4.1.2",
    '4_2_1': "Criteria 4.2.1",
    '4_3_1': "Criteria 4.3.1",
    '4_4_1': "Criteria 4.4.1",

    # criteria 5
    '5_1_1': "Criteria 5.1.1",
    '5_1_2': "Criteria 5.1.2",
    '5_1_3': "Criteria 5.1.3",
    '5_1_4': "Criteria 5.1.4",
    '5_2_1': "Criteria 5.2.1",
    '5_2_2': "Criteria 5.2.2",
    '5_3_1': "Criteria 5.3.1",
    '5_3_2': "Criteria 5.3.2",
    '5_4_1': "Criteria 5.4.1",

    # criteria 6
    '6_1_1': "Criteria 6.1.1",
    '6_2_1': "Criteria 6.2.1",
    '6_2_2': "Criteria 6.2.2",
    '6_3_1': "Criteria 6.3.1",
    '6_3_2': "Criteria 6.3.2",
    '6_3_3': "Criteria 6.3.3",
    '6_4_1': "Criteria 6.4.1",
    '6_5_1': "Criteria 6.5.1",
    '6_5_2': "Criteria 6.5.2",

    # criteria 7
    '7_1_1': "Criteria 7.1.1",
    '7_1_2': "Criteria 7.1.2",
    '7_1_3': "Criteria 7.1.3",
    '7_1_4': "Criteria 7.1.4",
    '7_2_1': "Criteria 7.2.1",
    '7_3_1': "Criteria 7.3.1",
}


def user_login(request):
    next_url = request.POST.get('next')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(username, password)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('home')
        else:
            if not CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'Invalid Username. User does not exist!')
            else:
                messages.error(request, 'Invalid password!')
    return render(request, 'login.html')


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Logout successfully!!')
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user_type = form.cleaned_data['user_type']
            username = form.cleaned_data['username']
            print(first_name)
            user = CustomUser.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                user_type=user_type
            )
            user.set_password(password)
            user.save()

            messages.success(request, 'Account created successfully!!')
            return redirect('login')
        else:
            if 'username' in form.errors:
                messages.error(request, 'Username already exists!!')
            elif 'email' in form.errors:
                messages.error(request, 'Email already exists!!')
            for error in form.non_field_errors():
                messages.error(request, error)
            return render(request, 'register.html', {'form': form})
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def profile(request, username):
    user = CustomUser.objects.get(username=username)
    tasks = UserCriteriaLink.objects.filter(user=user)
    context = {
        'user': user,
        'tasks': tasks,
    }
    return render(request, 'profile.html', context=context)


@login_required
def assign_user(request):
    user_criteria_links = UserCriteriaLink.objects.select_related('user').exclude(user__user_type='HOD').all()
    user_criteria_dict = defaultdict(lambda: {'assigned': [], 'unassigned': list(CRITERIA_LIST.values())})
    for link in user_criteria_links:
        user = link.user
        criteria = link.criteria
        readable_criteria = CRITERIA_LIST.get(criteria, criteria)
        user_criteria_dict[user]['assigned'].append(readable_criteria)
        if readable_criteria in user_criteria_dict[user]['unassigned']:
            user_criteria_dict[user]['unassigned'].remove(readable_criteria)
    all_users = CustomUser.objects.all()
    for user in all_users:
        if user not in user_criteria_dict:
            user_criteria_dict[user] = {'assigned': [], 'unassigned': list(CRITERIA_LIST.values())}
    context = {
        'users_list': user_criteria_dict.items(),
    }
    return render(request, 'assign_user.html', context=context)


REVERSE_CRITERIA_LIST = {v: k for k, v in CRITERIA_LIST.items()}


@login_required
def assign_user_to_criteria(request):
    username = request.POST.get('username')
    selected_criteria = request.POST.getlist('criteria')
    if username and selected_criteria:
        try:
            user = CustomUser.objects.get(username=username)
            assigned_criteria = []
            already_assigned_criteria = []
            invalid_criteria = []
            for criteria in selected_criteria:
                criteria_value = REVERSE_CRITERIA_LIST.get(criteria)
                if criteria_value:
                    user_criteria_link, created = UserCriteriaLink.objects.get_or_create(user=user,
                                                                                         criteria=criteria_value)
                    if created:
                        assigned_criteria.append(criteria)
                    else:
                        already_assigned_criteria.append(criteria)
                else:
                    invalid_criteria.append(criteria)
            if assigned_criteria:
                messages.success(request, f"Criteria assigned successfully: {', '.join(assigned_criteria)}.")

            if already_assigned_criteria:
                messages.warning(request, f"Criteria already assigned: {', '.join(already_assigned_criteria)}.")

            if invalid_criteria:
                messages.warning(request, f"Invalid criteria: {', '.join(invalid_criteria)}.")

            return redirect('assign_user')
        except CustomUser.DoesNotExist:
            messages.warning(request, "User not found.")
            return redirect('assign_user')
    else:
        messages.warning(request, "Invalid data. Please select criteria and ensure the user is valid.")
        return redirect('assign_user')


@login_required
def delete_user_to_criteria(request, username, criteria):
    print(criteria)
    criteria_key = REVERSE_CRITERIA_LIST.get(criteria)
    print(criteria_key)
    if username and criteria_key:
        try:
            user = CustomUser.objects.get(username=username)
            user_criteria_link = UserCriteriaLink.objects.get(user=user, criteria=criteria_key)
            user_criteria_link.delete()
            messages.success(request, "Criteria removed successfully.")
            return redirect('assign_user')
        except CustomUser.DoesNotExist:
            messages.warning(request, "User not found.")
            return redirect('assign_user')
        except UserCriteriaLink.DoesNotExist:
            messages.warning(request, "This criteria was not assigned to the user.")
            return redirect('assign_user')

    messages.warning(request, "Invalid data.")
    return redirect('assign_user')

